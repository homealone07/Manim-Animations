#https://discord.com/channels/581738731934056449/582403919754297363/952858739101290497
from cProfile import label
from ctypes.wintypes import LARGE_INTEGER
from re import S
from turtle import circle, down, left
from venv import create

from cairo import Surface
from manim import*
from manim.mobject import graph 

class Example_value_tracer(Scene):
    def construct(self):
        axes = (Axes(
                x_range=[0,15,1], x_length=7,
                y_range=[0,120,10], y_length=6,
                color = WHITE,

            ).add_coordinates().to_edge(LEFT,buff=0.2).shift(UP*0.2)
        )
        x_label = axes.get_x_axis_label("x=")
        y_label = axes.get_y_axis_label("f(x)")

        label = VGroup(x_label,y_label)
        
        func = axes.plot(lambda x: x**2, x_range = [0,12],color = YELLOW)


        self.play(Create(axes))
        self.play(Write(label),
                Create(func))

  

        dx = ValueTracker(1)
        x = ValueTracker(12)
        x = always_redraw(
            lambda: DecimalNumber().next_to(x_label).set_value(x.get_value())
        )
        tex = always_redraw(
            lambda: DecimalNumber().set_value(dx.get_value()))
        area1 = always_redraw( lambda:
            axes.get_riemann_rectangles(graph=func,
                                                    x_range=[0,x.get_value()],
                                                    dx = dx.get_value(),
                                                    input_sample_type='center', 
                                                    color=[GREEN,BLUE],
                                                    stroke_width = 0
                                                    ).set_opacity(1)
        )      
        self.play(Create(area1),
        Write(tex))

        self.play(dx.animate.set_value(0.01),run_time=3)
        self.play(x.animate.set_value(6))
