from manim import *

class ThreeDStream(Scene):
    def construct(self): #func = lambda u, v, w : [ 1, w , u**2 - w + 2*v ]
        func = lambda pos: ( 1 )*RIGHT + ( pos[2] )*UP + ( (pos[0])**2 - pos[2] + 2*pos[1] )*OUT
        stream_lines = StreamLines(func, stroke_width=3, max_anchors_per_line=30)
        self.add(stream_lines)
        stream_lines.start_animation(time_width = 2) #warm_up=False, flow_speed=1.5)
        self.wait(5) #stream_lines.virtual_time / stream_lines.flow_speed)
