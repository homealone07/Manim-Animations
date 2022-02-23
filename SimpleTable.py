from manim import *
class GetHighlightedCellExample(Scene):
    def construct(self):
        table = Table(
            [["First", "Second"],
            ["Third","Fourth"]],
            row_labels=[Text("R1"), Text("R2")],
            col_labels=[Text("C1"), Text("C2")])
        highlight = table.get_highlighted_cell((2,2), color=GREEN)
        table.add_to_back(highlight)
        #self.play(table.create())
        self.play(Create(table))
        self.wait()
