def construct(self):
    ax = Axes(
        x_range=[0, 8], 
        y_range=[-20, 60, 10], 
        x_axis_config={"numbers_to_include": np.arange(0, 8, 1)},
        y_axis_config={"numbers_to_include": np.arange(-20, 60, 10)}
    )
    labels = ax.get_axis_labels(x_label="t (s)", y_label=MathTex(r"\overrightarrow{F} (N)"))
    self.play(FadeIn(ax, labels))
    x_vals = [0, 1, 3, 5, 7, 8]
    y_vals = [0, 50, 30, -20, 10, 20]
    force_graph = ax.plot_line_graph(x_values=x_vals, y_values=y_vals, add_vertex_dots=False)
    self.play(Create(force_graph), run_time=5, rate_func=linear)
    self.wait(2)
    
    #https://discord.com/channels/581738731934056449/780234936980078602/963524148179656755
