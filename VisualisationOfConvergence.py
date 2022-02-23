import math

class Convergence(Scene):
    def construct(self):
        
        def epsilon_check(L, eps, val):
            if abs(val - L) < eps: return True
            else: return False
            
        def dot_updater(dot):
            if epsilon_check(a, e.get_value(), dot.val): 
                dot.set_color(GREEN) 
            else:
                dot.set_color(RED)
                
        num_of_terms = 20
        y_max = 4
        seq = [2 + 2* (-1)**n/n for n in range(1, num_of_terms + 1)]
        
        axes = Axes(x_range=[0,num_of_terms,1], 
                    y_range=[0,y_max,0.1],
                    x_length = 10, 
                    y_length = 5,
                    axis_config = {"include_ticks":False},
                    y_axis_config = {"include_numbers": False},
                    tips = False)
        axes.align_on_border(DOWN, buff=1)
        labels = VGroup(
            axes.get_x_axis_label(MathTex(r"n"), direction=DOWN),
            axes.get_y_axis_label(MathTex(r"x_n"),direction=LEFT)
            )
        self.play(Write(axes), Write(labels))
        
        dots = [Dot(point = axes.c2p(i, entry)).set(val=entry) for i, entry in enumerate(seq,1)]
        for dot in dots:
            self.play(Write(dot), run_time= 1.5/num_of_terms)
        
        self.wait(1)
        
        a = 2
        e = ValueTracker(0.6)
        alpha = MathTex(r"\alpha")
        alpha.move_to(axes.c2p(0, a) + LEFT * 0.2, aligned_edge = [1,0,0])
        dash = DashedLine(start=axes.c2p(0, a), end = axes.c2p(num_of_terms, a), dash_length=0.2, dashed_ratio = 0.7)
        
        epsilon_pos = always_redraw(
            lambda: 
                MathTex(r"\alpha + \varepsilon").move_to(
                    axes.c2p(0, a + e.get_value()) + LEFT * 0.2, 
                    aligned_edge = [1,0,0]
                )
        )
        dash_pos = always_redraw(lambda: DashedLine(start=axes.c2p(0, a + e.get_value()), end = axes.c2p(num_of_terms, a + e.get_value())))
        
        epsilon_neg = always_redraw(
            lambda: 
                MathTex(r"\alpha - \varepsilon").move_to(
                    axes.c2p(0, a - e.get_value()) + LEFT * 0.2, 
                    aligned_edge = [1,0,0]
                )
        )
        dash_neg = always_redraw(lambda: DashedLine(start=axes.c2p(0, a - e.get_value()), end = axes.c2p(num_of_terms, a - e.get_value())))
        
        N_pos = lambda: [epsilon_check(a, e.get_value(), dot.val) for dot in dots].index(True) + 1
        N = MathTex(r"N").move_to(axes.c2p(N_pos(),0) + DOWN * 0.2, aligned_edge=[0,1,0])
        N_dash = DashedLine(start=axes.c2p(N_pos(), 0), end=axes.c2p(N_pos(), y_max))
        
        eq1 = MathTex(r"\forall \varepsilon > 0")
        eq2 = MathTex(r"\exists N \in \mathbb{N}")
        eq3 = MathTex(r":\forall n \geq N")
        eq4 = MathTex(r"|x_n - \alpha| < \varepsilon")
        eqGroup = VGroup(eq1, eq2, eq3, eq4).arrange()
        eqGroup.align_on_border(UP)
        
        alp = VGroup(alpha, dash)
        eps_p = VGroup(epsilon_pos, dash_pos)
        eps_n = VGroup(epsilon_neg, dash_neg)
        Ngroup = VGroup(N, N_dash)
        
        rectCoords = [axes.c2p(num_of_terms, a + e.get_value()),
                      axes.c2p(0, a + e.get_value()),  
                      axes.c2p(0, a - e.get_value()),
                      axes.c2p(num_of_terms, a - e.get_value())]
        shadedRect = Polygon(*rectCoords, stroke_width=0, fill_color=YELLOW, fill_opacity=0.4)
        
        self.play(Write(alp), run_time = 0.75)
        self.wait(0.5)
        self.play(Write(eps_p), Write(eps_n))
        self.wait(0.75)
        self.play(FadeIn(eq1))
        self.wait(0.5)
        self.play(e.animate.set_value(0.3))
        self.play(e.animate.set_value(0.6))
        self.wait(0.75)
        self.play(FadeIn(eq2))
        self.wait(0.5)
        self.play(FadeIn(Ngroup))
        self.wait(1)
        self.play(FadeIn(eq3))
        self.wait(0.5)
        self.play(*[dot.animate.add_updater(dot_updater) for dot in dots], eq3.animate.set_color(GREEN))
        self.play(eq3.animate.set_color(WHITE))
        
        for dot in dots:
            dot.remove_updater(dot_updater)
            dot.add_updater(dot_updater)
        
        self.wait(1)
        self.play(FadeIn(eq4))
        self.wait(0.5)
        self.play(FadeIn(shadedRect), eq4.animate.set_color(YELLOW))
        self.play(FadeOut(shadedRect), eq4.animate.set_color(WHITE))
        self.wait(1.5)
        
        self.play(FadeOut(Ngroup))
        self.play(e.animate.set_value(0.25))
        Ngroup.set_x(axes.c2p(N_pos(),0)[0])
        self.play(FadeIn(Ngroup))
        
        self.wait(1)
        
        self.play(FadeOut(Ngroup))
        self.play(e.animate.set_value(0.8))
        Ngroup.set_x(axes.c2p(N_pos(),0)[0])
        self.play(FadeIn(Ngroup))
        
        self.wait(2)
