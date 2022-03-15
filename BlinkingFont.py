#https://discord.com/channels/581738731934056449/780234936980078602/951126239152857098
from manim import *
class Test(Scene):
    def construct(self):
        text = Text("One", font_size=144)
        self.play(Create(text))
        transform = Text("Two", font_size=144)
        self.play(ReplacementTransform(text, transform))
        self.wait()
        self.play(FadeOut(transform, shift=UP))

        
#2nd CODE
#https://discord.com/channels/581738731934056449/780234936980078602/951122704398950450
from manim import *
class Test(Scene):
    def construct(self):
        text = Text("Hello", font_size=144, color=RED)
        self.play(Create(text))
        self.play(FadeOut(text, shift=UP))
