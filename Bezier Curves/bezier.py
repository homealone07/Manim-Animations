class Bezier(ParametricFunction):
    def __init__(self, points, **kwargs):
        super().__init__(bezier(points),**kwargs)

class MainScene(Scene):
    def construct(self):
        points = [ np.array([x, y, 0])
            for x,y in [ (-5,2),  (-2,2), (-5,-3), (2,3), (4,3.2), (6,0), (6,-3),  (0,-1)]
        ]
        bezier_plot = Bezier(points)
        lines, dots = self.get_lines_and_dots_from_points(points)
        init_grp = VGroup(VGroup(lines, dots))
        all_grp = self.get_all_lines(init_grp.copy(), 0)

        self.add(all_grp)
        self.wait()
        self.play(
            UpdateFromAlphaFunc(all_grp,
                lambda mob, alpha: mob.become(
                    self.get_all_lines(init_grp.copy(), alpha)
                )
            ),
            Create(bezier_plot),
            run_time=10, rate_func=linear
        )
        self.wait()

    def get_lines_and_dots_from_points(self, points):
        lines = VGroup(*[
            Line(points[i],points[i+1])
            for i in range(len(points)-1)
        ])
        dots = VGroup(*list(map(Dot,points)))
        return lines, dots

    def get_sub_lines(self, lines, alpha):
        points = [
            l.point_from_proportion(alpha)
            for l in lines
        ]
        new_lines, dots =  self.get_lines_and_dots_from_points(points)
        return VGroup(new_lines, dots)

    def get_all_lines(self, main_grp, alpha, index=0):
        last_grp = main_grp[-1]
        new_lines = last_grp[0]
        if len(new_lines) >= 2:
            main_grp.add( self.get_sub_lines(new_lines, alpha) )
            return self.get_all_lines(main_grp, alpha, index+1)
        else:
            main_grp.add( Dot(new_lines[0].point_from_proportion(alpha)) )
            return main_grp
