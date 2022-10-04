def construct(self):
        axes = Axes([-10, 10, 1], [-20, 20, 2], 8,
                    8).add_coordinates(font_size=16)

        pq_gen = MathTex(
            r"x_{\text{1/2}} = -\frac{p}{2} \pm \sqrt{\left(\frac{p}{2}\right)-q}")

        graph = axes.plot(lambda x: x**2+5*x-7, [-8, 3], color=BLUE)

        func_label = MathTex(
            "f(x)=x^2+", "5", "x", "-7", font_size=22).next_to(graph, RIGHT, 0.3)

        plot = VGroup(axes, graph, func_label)
        self.play(Write(graph), DrawBorderThenFill(
            axes), Write(func_label), run_time=5)
        self.wait(2)
        self.play(plot.animate.scale(0.5).shift(UP*1.8 + LEFT*4.9))
        self.play(Write(pq_gen), run_time=5)
        self.play(pq_gen.animate.to_edge(UR, buff=0.5))
        self.play(func_label.animate.move_to(ORIGIN).scale(4))

        framebox_p = SurroundingRectangle(func_label[1], YELLOW, 0.1)
        framebox_q = SurroundingRectangle(func_label[3], YELLOW, 0.1)
        p = Tex("p").next_to(framebox_p, DOWN, buff=0.2)
        q = Tex("q").next_to(framebox_q, DOWN, buff=0.2)

        self.play(Create(framebox_p))
        self.play(Write(p))
        self.wait()
        self.play(Unwrite(p))
        self.play(ReplacementTransform(framebox_p, framebox_q))
        self.play(Write(q))
        self.wait()
        self.play(Unwrite(q))
        self.play(Uncreate(framebox_q))
        self.wait(0.5)
        self.play(func_label.animate.scale(0.25).next_to(graph, RIGHT, 0.3))
