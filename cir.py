from manim import *
class ChangeShape(Scene):
    def construct(self):
        circle = Circle()
        circle.set_fill(BLUE, opacity=0.5) # set the color and transparency
        circle.flip(RIGHT)
        self.play(GrowFromCenter(circle))
         self.wait(2)
        square = Square()
        square.set_fill(YELLOW, opacity=0.5)
        square.flip(RIGHT)
        self.play(Transform(circle, square)) # turn the circle into a square
        self.wait(2)
        triangle = Triangle()
        triangle.set_fill(GREEN, opacity=0.5)
        triangle.flip(RIGHT)
        self.play(Transform(circle, triangle)) # turn the square into a triangle
        self.wait(2)
        ellipse= Ellipse()
        ellipse.set_fill(RED, opacity=0.5)
        ellipse.flip(RIGHT)
        self.play(Transform(circle, ellipse)) # turn triangle into Ellipse
        self.wait(2)