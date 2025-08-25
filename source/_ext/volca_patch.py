from __future__ import annotations

from docutils import nodes

from sphinx.application import Sphinx
from sphinx.util.docutils import SphinxDirective, SphinxRole
# from sphinx.util.typing import ExtensionMetadata


class HelloRole(SphinxRole):
    """A role to say hello!"""

    def run(self) -> tuple[list[nodes.Node], list[nodes.system_message]]:
        node = nodes.inline(text=f'Hello {self.text}!')
        return [node], []


class DrumKitPart(SphinxDirective):
    """A directive to say hello!"""

    # required_arguments = 1
    has_content = True

    def run(self) -> list[nodes.Node]:
        # {{{ TABLE_DATA
        d = [ l.strip().split() for l in self.content if l.strip()]

        src1     = d[0][0].upper()
        lvl1     = d[0][1]
        pitch1   = d[0][2]
        mod1     = d[1][0].upper()
        amt1     = d[1][1]
        rate1    = d[1][2]
        eg1      = d[2][0].upper()
        attack1  = d[2][1]
        release1 = d[2][2]
        
        src2     = d[3][0].upper()
        lvl2     = d[3][1]
        pitch2   = d[3][2]
        mod2     = d[4][0].upper()
        amt2     = d[4][1]
        rate2    = d[4][2]
        eg2      = d[5][0].upper()
        attack2  = d[5][1]
        release2 = d[5][2]

        bit      = d[6][0]
        fld      = d[6][1]
        drw      = d[6][2]
        pan      = d[7][0]
        gan      = d[7][1]
        snd      = d[7][2]
        
        table_data = [
                ["", "Layer 1", "Layer 2", "Processing"],
                ["LVL", lvl1, lvl2] + [bit],
                ["PITCH", pitch1, pitch2] + [fld],
                ["SRC", src1, src2] + [drw],
                ["MOD", mod1, mod2] + [pan],
                ["EG", eg1, eg2] + [gan],
                ["AMT", amt1, amt2] + [snd],
                ["RATE", rate1, rate2],
                ["ATT", attack1, attack2],
                ["REL", release1, release2],
                ]
# }}}
        table = nodes.table()# {{{

        tgroup = nodes.tgroup(cols=len(table_data[0]))
        table += tgroup

        # Column specifications
        for _ in range(len(table_data[0])):
            tgroup += nodes.colspec(colwidth=1)

        # Table body
        tbody = nodes.tbody()
        tgroup += tbody

        for row in table_data:
            row_node = nodes.row()
            for cell in row:
                entry = nodes.entry()
                entry += nodes.paragraph(text=cell)
                row_node += entry
            tbody += row_node

        # }}}
        return [table]


def setup(app: Sphinx): # -> ExtensionMetadata:{{{
    app.add_role('hello', HelloRole())
    app.add_directive('drumkitpart', DrumKitPart)

    return {
        'version': '0.1',
        'parallel_read_safe': True,
        'parallel_write_safe': True,
    }
# }}}

