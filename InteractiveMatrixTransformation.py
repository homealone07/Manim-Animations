from manim import *
from manim.utils.space_ops import shoelace

def point_to_mobject(self, point, search_set=None):
    # E.g. if clicking on the scene, this returns the top layer mobject
    # under a given point
    if search_set is None:
        search_set = self.mobjects
    for mobject in reversed(search_set):
        if mobject.is_point_touching(point):
            return mobject
    return None


Scene.point_to_mobject = point_to_mobject


class Test(Scene):
    def construct(self):
        A = Dot([1, 0, 0])
        B = Dot([0, 1, 0])
        plane = always_redraw(
            lambda: NumberPlane().apply_matrix(np.array([A.get_center()[:2], B.get_center()[:2]]).T)
        )
        vecs = VGroup(
            always_redraw(lambda: Vector(A.get_center(), color=RED)),
            always_redraw(lambda: Vector(B.get_center(), color=GREEN)),
        )
        det = always_redraw(
            lambda: Polygon(ORIGIN, A.get_center(), A.get_center() + B.get_center(), B.get_center(), fill_opacity=0.4, color=YELLOW)
        )
        num = always_redraw(lambda: DecimalNumber(-shoelace(det.points)).to_corner(UL))
        self.add(plane, det, vecs, num, A, B)

        self.interactive_embed()

    def on_mouse_motion(self, point, d_point):
        super().on_mouse_motion(point, d_point)
        self.mouse_point.move_to(point)
        from pyglet.window import key

        if key.A in self.renderer.pressed_keys:  # Move the object by holding down 'A'
            mob = self.point_to_mobject(point)
            if mob is None:
                return
            mob.move_to(self.mouse_point)
 
#Then in the console, run:
#manim file_name.py -p --renderer opengl
#To move the dots, press 'a' on the dot and move the mouse.
