#https://discord.com/channels/581738731934056449/780234936980078602/951846466291400815

class PolygonOnPlot(Scene):
    def get_rectangle_coors(self, bottom_left, top_right):
        return [
            (top_right[0], top_right[1]),
            (bottom_left[0], top_right[1]),
            (bottom_left[0], bottom_left[0]),
            (top_right[0], bottom_left[0]),
        ]

    def construct(self):
        ax = Axes(
            x_range=[0, 10],
            y_range=[0, 10],
            x_length=6,
            y_length=6,
            axis_config={"include_tip": False},
        )

        t = ValueTracker(5)
        k = 25

        graph = always_redraw(
            lambda: ax.plot(
                lambda x: k / x,
                color=YELLOW_D,
                x_range=[
                    k / 10,
                    10.0,
                    0.01,
                ],
                use_smoothing=False,
            )
        )

        def get_rectangle():
            polygon = Polygon(
                *[
                    ax.c2p(*i)
                    for i in self.get_rectangle_coors(
                        (0, 0), (t.get_value(), k / t.get_value())
                    )
                ]
            )
            polygon.stroke_width = 1
            polygon.set_fill(BLUE, opacity=0.5)
            polygon.set_stroke(YELLOW_B)
            return polygon

        polygon = always_redraw(get_rectangle)

        dot = Dot()
        dot.add_updater(lambda x: x.move_to(ax.c2p(t.get_value(), k / t.get_value())))
        dot.set_z_index(10)

        self.add(ax)
        self.wait(0.5)
        self.play(Create(graph))
        self.play(Create(dot))
        self.wait(1)
        self.play(Create(polygon))
        self.wait(1)
        self.play(t.animate.set_value(10))
        self.wait(1)
        self.play(t.animate.set_value(k / 10))
        self.wait(1)
        self.play(t.animate.set_value(5))
        self.wait(3)
