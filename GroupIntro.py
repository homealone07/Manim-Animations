#First Code
from manim import *

class UnwriteReverseFalse(Scene):
    def construct(self):
        text = Tex("Hello we are team").scale(3)
        self.add(text)
        self.wait(0.5)
        self.play(Unwrite(text, reverse=False))
        r = Tex("H","E","L","I","X").scale(2.5)
        r[0].set_color(RED)
        r[1].set_color(BLUE)
        r[2].set_color(YELLOW)
        r[3].set_color(GREEN)
        r[4].set_color(ORANGE)
        self.play(Write(r),run_time=3)
        self.play(Unwrite(r, reverse=False))
        sd = Tex("ABHAY ARORA", color = RED).scale(2)
        sds = Tex('20BRS1224', color = BLUE).scale(1.75)
        self.play(
            Create(sd),
            run_time=1
        )
        self.play(
            Transform(
                sd,sds
            ),
            run_time=1.25
        )
        self.play(
            Unwrite(
                VGroup(
                    sd,sds
                )
            ),
            run_time=1
        )
        sd = Tex('Venkat Amith Woonna', color = RED).scale(2)
        sds = Tex('20BCE1222', color = BLUE).scale(1.75)
        self.play(
            Create(sd),
            run_time=1
        )
        self.play(
            Transform(
                sd,sds
            ),
            run_time=1.25
        )
        self.play(
            Unwrite(
                VGroup(
                    sd,sds
                )
            ),
            run_time=1
        )
        sd = Tex("Gaurav Jena", color = RED).scale(2)
        sds = Tex('20BCE1233', color = BLUE).scale(1.75)
        self.play(
            Create(sd),
            run_time=1
        )
        self.play(
            Transform(
                sd,sds
            ),
            run_time=1.25
        )
        self.play(
            Unwrite(
                VGroup(
                    sd,sds
                )
            ),
            run_time=1
        )
        sd = Tex('Vamsi Vikkurty', color = RED).scale(2)
        sds = Tex('20BCE1066', color = BLUE).scale(1.75)
        self.play(
            Create(sd),
            run_time=1
        )
        self.play(
            Transform(
                sd,sds
            ),
            run_time=1.25
        )
        self.play(
            Unwrite(
                VGroup(
                    sd,sds
                )
            ),
            run_time=1
        )
        sd = Tex('Sai Kailash', color = RED).scale(2)
        sds = Tex('20BRS1208', color = BLUE).scale(1.75)
        self.play(
            Create(sd),
            run_time=1
        )
        self.play(
            Transform(
                sd,sds
            ),
            run_time=1.25
        )
        self.play(
            Unwrite(
                VGroup(
                    sd,sds
                )
            ),
            run_time=1
        )

        
#2nd Code

from manim import *

class UnwriteReverseFalse(Scene):
    def construct(self):
        text = Tex("Hello we are team").scale(3)
        self.add(text)
        self.wait(0.5)
        self.play(Unwrite(text, reverse=False))
        r = Tex("H","E","L","I","X").scale(2.5)
        r[0].set_color(RED)
        r[1].set_color(BLUE)
        r[2].set_color(YELLOW)
        r[3].set_color(GREEN)
        r[4].set_color(ORANGE)
        self.play(Write(r),run_time=3)
        self.play(Unwrite(r, reverse=False))
        self.play(Unwrite(text, reverse=False))
        text = Tex("Abhay Arora" , color = RED).scale(2)
        reg = Tex("20BRS1224" , color = BLUE).scale(2)
        self.add(text)
        self.wait(0.6)
        self.play(Unwrite(text))
        self.add(reg)
        self.wait(0.6)
        self.play(Unwrite(reg))
        text = Tex("Venkat Amith Woonna" , color = RED).scale(2)
        reg = Tex("20BCE1222" , color = BLUE).scale(2)
        self.add(text)
        self.wait(0.6)
        self.play(Unwrite(text))
        self.add(reg)
        self.wait(0.6)
        self.play(Unwrite(reg))
        text = Tex("Gaurav Jena" , color = RED).scale(2)
        reg = Tex("20BCE1233" , color = BLUE).scale(2)
        self.add(text)
        self.wait(0.6)
        self.play(Unwrite(text))
        self.add(reg)
        self.wait(0.6)
        self.play(Unwrite(reg))
        text = Tex("Sai Kailash" , color = RED).scale(2)
        reg = Tex("20BRS1208" , color = BLUE).scale(2)
        self.add(text)
        self.wait(0.6)
        self.play(Unwrite(text))
        self.add(reg)
        self.wait(0.6)
        self.play(Unwrite(reg))
        text = Tex("Vamsi Vikkurty" , color = RED).scale(2)
        reg = Tex("20BCE1066" , color = BLUE).scale(2)
        self.add(text)
        self.wait(0.6)
        self.play(Unwrite(text))
        self.add(reg)
        self.wait(0.6)
        self.play(Unwrite(reg, reverse=False))
