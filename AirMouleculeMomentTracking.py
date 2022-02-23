class Molecules(Scene):
    def construct(self):
        dots = [Dot()for i in range(15)]

        b = VGroup(dots[0], dots[1], dots[2], dots[3], dots[4], dots[5], dots[6], dots[7], dots[8], dots[9], dots[10], dots[11], dots[12], dots[13], dots[14])
        b.arrange(RIGHT, buff=1)

        self.add(*dots)

        for j in range(14):
            self.play(dots[j].animate.shift(LEFT*0.2), dots[j+1].animate.shift(RIGHT*1.2), run_time=0.3, rate_func=linear)

        self.wait()
