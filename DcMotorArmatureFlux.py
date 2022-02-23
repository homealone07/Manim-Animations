from manim import *
from manim_physics import *

def field_func(p, *currents):
    direction = np.zeros(3)
    pos = []
    for current in currents:
        x, y, z = p
        x0, y0, z0 = point = current.get_center()
        mag = current.magnitude
        pos.append(point)
        if (x - x0) ** 2 > 0.01 or (y - y0) ** 2 > 0.01:
            dist = np.linalg.norm(p - point)
            direction += mag * np.array([-(y - y0), (x - x0), 0]) / dist ** 3
        else:
            direction += np.zeros(3)
    for p0 in pos:
        if all(p == p0):
            direction = np.zeros(3)
    return direction

class DcMotor(ZoomedScene,Scene):
    def construct(self):

        armature = Circle(
            radius=1.5,
            fill_opacity=1, 
            fill_color= BLACK,
            stroke_color=WHITE)

        stator = Circle(
            radius=1.7,
            fill_opacity=1, 
            fill_color= BLACK,
            stroke_color=WHITE)
        
        mob = DashedLine(color= YELLOW)
        c1 = Current(armature.get_top()-UP*0.3  ,direction=OUT)
        c2 = Current(armature.get_bottom()+UP*0.3,direction=IN)
        
        Motor_base = VGroup(stator,armature,c1,c2)        
        
        field = CurrentMagneticField(c1,c2,
        length_func = lambda norm: 0.3 * sigmoid(norm),
        min_color_scheme_value=2,
        max_color_scheme_value=10
        )

        flux = StreamLines(lambda p: field_func(p,c1,c2),max_anchors_per_line=50)
        self.add(Motor_base)
        
        self.add(flux)
        # flux.start_animation(warm_up=False, flow_speed=1.5)
        # self.wait(flux.virtual_time / flux.flow_speed)
        
