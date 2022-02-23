from numpy import heaviside, square
from manim import *
import math


def get_hexagon_tiling(x_min=-6, x_max=6, y_min=-3, y_max=3, **kwargs):
    tiles = VGroup()
    for x in range(x_min, x_max):
        for y in range(y_min, y_max):
            if x % 2 == 1:
                y += 0.5
            y *= math.sqrt(3)
            hexagon = RegularPolygon(**kwargs)
            hexagon.move_to(x * 1.5 * RIGHT + y * UP)
            tiles.add(hexagon)
    return tiles


def get_dodecagon_tiling(x_min=-10, x_max=10, y_min=-2, y_max=2, **kwargs):
    tiles = VGroup()
    for x in range(x_min, x_max):
        for y in range(y_min, y_max):
            if x % 2 == 1:
                y += 0.5
            y *= 3 + math.sqrt(27)
            dodecagon = RegularPolygon(n=12, start_angle=15 * DEGREES, **kwargs)
            dodecagon.scale(math.sqrt(0.5) + math.sqrt(1.5))
            center = x * (1.5 + math.sqrt(0.75)) * RIGHT + y * UP
            dodecagon.move_to(center)
            tiles.add(dodecagon)
            for angle in (-60, 0, 60):
                angle *= DEGREES
                square = Square(side_length=1, **kwargs)
                square.rotate(angle)
                square.move_to(center)
                square.shift(rotate_vector((1.5 + math.sqrt(0.75)) * RIGHT, angle))
                tiles.add(square)
                angle += 30 * DEGREES
                hexagon = RegularPolygon(**kwargs)
                hexagon.move_to(center)
                hexagon.shift(rotate_vector((1 + math.sqrt(3)) * RIGHT, angle))
                tiles.add(hexagon)
    return tiles



class HexagonTiling(MovingCameraScene):
    def construct(self):
        hexagons = get_hexagon_tiling(stroke_color=YELLOW, stroke_width=2)
        self.play(ShowIncreasingSubsets(hexagons))
        self.wait()
        self.play(self.camera.frame.animate.scale(2))
        self.wait()


class DodecagonTiling(MovingCameraScene):
    def construct(self):
        dodecagons = get_dodecagon_tiling(
            stroke_color=YELLOW, 
            stroke_width=5, 
            fill_opacity=0,
        )
        anims = []
        for shape in sorted(dodecagons, key=lambda mob: np.linalg.norm(mob.get_center())):
            anims.append(FadeIn(shape))
        self.camera.frame.scale(5)
        self.play(AnimationGroup(*anims, lag_ratio=0.02))
        self.wait()


