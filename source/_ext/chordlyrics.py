from docutils import nodes
from docutils.parsers.rst import Directive
import re

class ChordLyricsDirective(Directive):
    has_content = True

    def run(self):
        lines = []

        chord_pattern = re.compile(r"\[([^\]]+)\]")   # [Chord]
        bare_pattern = re.compile(r"<([^>]+)>")       # <Chord>

        for rawline in self.content:
            stripped = rawline.strip()

            # Comment line
            if stripped.startswith("#"):
                text = stripped.lstrip("#").strip()
                lines.append(f'<div class="lyrics-comment">{text}</div>')
                continue

            # Instrumental line (contains <...>)
            if bare_pattern.search(rawline):
                html_line = '<div class="instrumental-line">'
                pos = 0
                while pos < len(rawline):
                    m = bare_pattern.search(rawline, pos)
                    if m:
                        chord = m.group(1)
                        start, end = m.span()
                        if start > pos:
                            html_line += rawline[pos:start]
                        html_line += f'<span class="instrumental-chord">{chord}</span>'
                        pos = end
                    else:
                        html_line += rawline[pos:]
                        break
                html_line += "</div>"
                lines.append(html_line)
                continue

            # Normal lyric line with [Chord]
            html_line = '<div class="lyrics-line">'
            pos = 0
            while pos < len(rawline):
                m = chord_pattern.search(rawline, pos)
                if m:
                    chord = m.group(1)
                    start, end = m.span()
                    if start > pos:
                        html_line += rawline[pos:start]
                    word_match = re.match(r'\S+', rawline[end:])
                    if word_match:
                        word = word_match.group(0)
                        html_line += f'<span class="chord-anchor"><span class="chord">{chord}</span>{word}</span>'
                        pos = end + len(word)
                    else:
                        html_line += f'<span class="chord-anchor"><span class="chord">{chord}</span></span>'
                        pos = end
                else:
                    html_line += rawline[pos:]
                    break
            html_line += "</div>"
            lines.append(html_line)

        html = "\n".join(lines)
        node = nodes.raw('', html, format='html')
        return [node]


def setup(app):
    app.add_directive("chordlyrics", ChordLyricsDirective)

