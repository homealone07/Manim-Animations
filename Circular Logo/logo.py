class example(Scene):
    def construct(self):
        C1 = Circle(fill_color=RED, z_index=1).shift(LEFT*0.25)
        C2 = Circle(fill_color=BLUE, z_index=0).shift(RIGHT*0.25)
        self.play(
            Create(C1),
            Create(C2)
            )
