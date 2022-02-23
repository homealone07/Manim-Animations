from manim import *
class Escena(Scene):
    def construct(self):
        svg1 = SVGMobject('cara externa 1.svg').scale(3).set_color(BLUE)
        svg2 = SVGMobject('cara externa 2.svg').scale(3).set_color(PINK)
        svg3 = SVGMobject('caras internas 1.svg').scale(3).set_color(YELLOW_C)
        svg4 = SVGMobject('caras internas 2.svg').scale(3).set_color(BLACK)
        self.camera.background_color =WHITE
        self.play(Create(svg1), run_time=1)
        self.wait(0.5)
        self.play(Transform(svg1,svg2), run_time=1)
        self.wait(0.5)
        self.play(Transform(svg1,svg3), run_time=1)
        self.wait(0.5)
        self.play(Transform(svg1,svg4), run_time=1)
        self.wait(0.5)
        self.play(FadeOut(svg1))
        


        
