# from docutils import nodes
# from docutils.parsers.rst import Directive

# class ChordLyricsDirective(Directive):
#     has_content = True

#     def run(self):
#         lines = []
#         for line in self.content:
#             html = ""
#             i = 0
#             while i < len(line):
#                 if line[i] == "[":
#                     j = line.find("]", i)
#                     if j != -1:
#                         chord = line[i+1:j]
#                         html += f'<span class="chord">{chord}</span>'
#                         i = j + 1
#                         continue
#                 html += line[i]
#                 i += 1
#             lines.append(html)
#         node = nodes.raw('', '<br/>'.join(lines), format='html')
#         return [node]

# def setup(app):
#     app.add_directive("chordlyrics", ChordLyricsDirective)


# ----------------------------------------

# from docutils import nodes
# from docutils.parsers.rst import Directive

# class ChordLyricsDirective(Directive):
#     has_content = True

#     def run(self):
#         lines = []

#         for rawline in self.content:
#             html_line = '<div class="lyrics-line">'
#             i = 0
#             while i < len(rawline):
#                 if rawline[i] == "[":
#                     j = rawline.find("]", i)
#                     if j != -1:
#                         chord = rawline[i+1:j]
#                         html_line += f'<span class="chord-anchor"><span class="chord">{chord}</span>'
#                         i = j + 1
#                         continue
#                 # normal character
#                 html_line += rawline[i]
#                 i += 1
#             # close any chord-anchor left open
#             if html_line.endswith("</span>") is False:
#                 html_line += "</span>" if "<span class=\"chord-anchor\">" in html_line else ""
#             html_line += "</div>"
#             lines.append(html_line)

#         html = "\n".join(lines)
#         node = nodes.raw('', html, format='html')
#         return [node]

# def setup(app):
#     app.add_directive("chordlyrics", ChordLyricsDirective)



# ----------------------------------------


# from docutils import nodes
# from docutils.parsers.rst import Directive
# import re

# class ChordLyricsDirective(Directive):
#     has_content = True

#     def run(self):
#         lines = []

#         chord_pattern = re.compile(r"\[([^\]]+)\]")  # matches [Chord]

#         for rawline in self.content:
#             html_line = '<div class="lyrics-line">'
#             pos = 0
#             while pos < len(rawline):
#                 m = chord_pattern.search(rawline, pos)
#                 if m:
#                     chord = m.group(1)
#                     start, end = m.span()
#                     # Add any text before the chord
#                     if start > pos:
#                         html_line += rawline[pos:start]
#                     # Find the following word (letters, numbers, punctuation)
#                     word_match = re.match(r'\S+', rawline[end:])
#                     if word_match:
#                         word = word_match.group(0)
#                         html_line += f'<span class="chord-anchor"><span class="chord">{chord}</span>{word}</span>'
#                         pos = end + len(word)
#                     else:
#                         # Chord at end of line without word
#                         html_line += f'<span class="chord-anchor"><span class="chord">{chord}</span></span>'
#                         pos = end
#                 else:
#                     # No more chords, add remaining text
#                     html_line += rawline[pos:]
#                     break

#             html_line += "</div>"
#             lines.append(html_line)

#         html = "\n".join(lines)
#         node = nodes.raw('', html, format='html')
#         return [node]


# def setup(app):
#     app.add_directive("chordlyrics", ChordLyricsDirective)



# ----------------------------------------


# from docutils import nodes
# from docutils.parsers.rst import Directive
# import re

# class ChordLyricsDirective(Directive):
#     has_content = True

#     def run(self):
#         lines = []
#         chord_pattern = re.compile(r"\[([^\]]+)\]")  # matches [Chord]

#         for rawline in self.content:
#             stripped = rawline.strip()

#             # Handle comment lines beginning with "#"
#             if stripped.startswith("#"):
#                 text = stripped.lstrip("#").strip()
#                 html_line = f'<div class="lyrics-comment">{text}</div>'
#                 lines.append(html_line)
#                 continue

#             # Normal lyric line with chords
#             html_line = '<div class="lyrics-line">'
#             pos = 0
#             while pos < len(rawline):
#                 m = chord_pattern.search(rawline, pos)
#                 if m:
#                     chord = m.group(1)
#                     start, end = m.span()
#                     if start > pos:
#                         html_line += rawline[pos:start]
#                     word_match = re.match(r'\S+', rawline[end:])
#                     if word_match:
#                         word = word_match.group(0)
#                         html_line += f'<span class="chord-anchor"><span class="chord">{chord}</span>{word}</span>'
#                         pos = end + len(word)
#                     else:
#                         html_line += f'<span class="chord-anchor"><span class="chord">{chord}</span></span>'
#                         pos = end
#                 else:
#                     html_line += rawline[pos:]
#                     break
#             html_line += "</div>"
#             lines.append(html_line)

#         html = "\n".join(lines)
#         node = nodes.raw('', html, format='html')
#         return [node]

# def setup(app):
#     app.add_directive("chordlyrics", ChordLyricsDirective)




# ----------------------------------------


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

