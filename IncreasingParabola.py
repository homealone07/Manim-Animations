#https://discord.com/channels/581738731934056449/582403919754297363/952492189412384769
class ExponentialDecay(Scene):
    def construct(self):
        x = ValueTracker(0.1)
        tau = np.log(2)
        t0 = always_redraw(lambda : DecimalTable(
            [np.array([x.get_value() - .1]), np.exp(np.array([x.get_value() - .1]) * tau)],
            row_labels=[Text("Percentage of Completion"), Text("Time in Weeks")],
            h_buff=1,
            element_to_mobject_config={"num_decimal_places": 2}).to_edge(UR, buff = .5).scale(.8))
        
        axes = Axes(x_range = [0, 5], y_range = [0, 105, 5], x_length = 4, y_length = 4).add_coordinates()
        graph = always_redraw(lambda : axes.plot(lambda x : np.exp(tau * x), x_range = [0, x.get_value()]))
        
        self.add(t0)
        self.play(Create(axes), Write(graph))
        self.play(x.animate.set_value(5.1), run_time = 10)
        self.wait()
