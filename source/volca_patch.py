from docutils import nodes
from docutils.parsers.rst import Directive

class VolcaPatchDirective(Directive):
    has_content = True

    def run(self):# {{{
        # Each line is a row of numbers
        table_data = [line.strip().split() for line in self.content if line.strip()]
        print("Q"*77)
        
        table = nodes.table()

        tgroup = nodes.tgroup(cols=len(table_data[0]))
        tgroup = nodes.tgroup(7)
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
                entry += nodes.paragraph(text="cell")
                row_node += entry
            tbody += row_node

        return table
# }}}

    def run2(self):# {{{
        # Each line is a row of numbers
        table_data = [line.strip().split() for line in self.content if line.strip()]
        
        table = nodes.table()

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

        return table
# }}}
