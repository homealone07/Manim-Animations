from manim import *
import mpmath

mpmath.mp.dps = 7


def zeta(s):
    max_norm = (8.0 * (16.0 / 9.0)) / 2

    try:
        return complex(mpmath.zeta(s))
    except:
        return complex(max_norm, 0)


class ZetaTest(Scene):
    def construct(self):
        plane = ComplexPlane(x_line_frequency=0.5, y_line_frequency=0.5)

        self.play(Write(plane))
        self.wait()

        plane.prepare_for_nonlinear_transform()
        self.play(
            plane.animate.apply_complex_function(
                lambda p: zeta(p)
            )
        )
        self.wait()
