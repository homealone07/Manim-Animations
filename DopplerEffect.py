from manim import *
import numpy as np

current_frame = 0

class Doppler(Scene):

    def construct(self):
        
        source=Dot()
        
        #creates a group to store the wavefronts
        waves=VGroup() 

        
        #function to add each wavefront
        def addwavefront(mob,dt):

            global current_frame

            wavefront=Circle(
                radius=0.01,
                color=YELLOW,
                stroke_width=1.5,
                arc_center=source.get_center()
            ) 
            current_frame += 1
            if current_frame%8 == 0: #frequency of the wave
                waves.add(wavefront)
            return current_frame

        #function to expand and fade away each wavefront
        def expandwaves(mob, dt):

            for wavefront in waves:
                wavefront.scale_to_fit_width(wavefront.width + 0.055)#wave speed
                wavefront.set_stroke(opacity = 1 - wavefront.width/20)
                if (1 - wavefront.width/20) == 0:
                    waves.remove(wavefront)
    

        waves.add_updater(addwavefront)
        waves.add_updater(expandwaves)

        self.add(source)
        self.add(waves)

        self.wait(2)
        self.play(
                source.animate.shift(RIGHT*5), rate_func=linear, run_time=10
        )
        self.play(
                source.animate.shift(LEFT*8), run_time=5
        )
        waves.remove_updater(addwavefront)
        self.wait(1)
        self.play(FadeOut(waves), FadeOut(source))
        self.wait(1)
        
#if you want to change the frequency of pulse emission, 
#you need to simply change the number after % in the  if current_frame%8 == 0: line
