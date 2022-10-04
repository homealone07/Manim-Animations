class multiplication(Scene):
    def construct(self):
            a = 3
            theTable = []
            for b in range(10):
                theTable.append([a, r"\times", b+1, r"=", a*(b+1)])
            texTable = MathTable(theTable,include_outer_lines=False).scale(0.6).to_edge(UP)
            texTable.remove(*texTable.get_vertical_lines())
            texTable.remove(*texTable.get_horizontal_lines())

            self.play(Write(texTable))

            self.wait(5)
            self.remove(texTable)
