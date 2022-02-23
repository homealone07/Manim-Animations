class BarChartExample(Scene):
    def construct(self):
        pull_req = [54, 23, 47, 48, 40, 64, 112, 87]
        versions = [
            "v0.1.0",
            "v0.1.1",
            "v0.2.0",
            "v0.3.0",
            "v0.4.0",
            "v0.5.0",
            "v0.6.0",
            "v0.7.0",
        ]
        colors = ["#003f5c", "#58508d", "#bc5090", "#ff6361", "#ffa600"]
        bars = BarChart(
            pull_req,
            max_value=max(pull_req),
            bar_colors=colors,
            bar_names=versions,
            bar_label_scale_val=0.3,
        )
        for bar in bars:
            self.play(Create(bar))
