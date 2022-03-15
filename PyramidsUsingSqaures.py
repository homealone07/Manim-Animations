#https://discord.com/channels/581738731934056449/780234936980078602/951206764630638613
from manim import *
import itertools as it

class Pyramid(ThreeDScene):
    def construct(self):

        a = 0.7 # длина стороны кубика     
        n = 5 # высота пирамиды (в кубиках)

        Pyramid = VGroup()
        d = [i for i in range(n)]        
        for k, j, i in it.product(d, d, d): 
            if (k+i <= n-1) and (k+j <= n-1):  
                cube = Cube(side_length=a).set_fill(BLUE_D, opacity=1).set_stroke(WHITE, 1)                    
                Pyramid.add(cube.shift(a*(RIGHT*i + DOWN*j + OUT*k)))  

        self.set_camera_orientation(phi=PI/3, theta=-PI/3, focal_distance=500)        
        self.play(Write(Pyramid))
        self.wait(3)
