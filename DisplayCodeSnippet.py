class TestCode(Scene):
    def construct(self):
        rendered_code = Code(code="print(\"Hello world!\")", tab_width=4, background="window", language="Python", font="Monospace")
        self.play(Create(rendered_code))
