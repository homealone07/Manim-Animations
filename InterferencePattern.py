from manimlib import *
class Interference(Scene):
    def construct(self):
        d = 15
        t = ValueTracker(0)
        a = always_redraw(lambda:ParametricSurface(lambda u,v:
            np.array([
                u,v,
                np.sin(((u-d)**2+(v-100)**2)**0.5-5*t.get_value())+
                np.sin(((u+d)**2+(v-100)**2)**0.5-5*t.get_value())
            ]),
            u_range = [-100,100],
            v_range = [-100,100],
        ).set_color(BLUE))
        self.add(a)
        fr = self.camera.frame
        fr.set_euler_angles(theta=PI/2,phi=PI/3)
        fr.scale(20)
        self.play(t.animate.set_value(10),rate_func=linear,run_time=10)
