from manim import *


class Test(Scene):
  def construct(self):

    intro = MathTex(r"1+1=2", r"\\2+2=4")

    equations1 = MathTex(r"ax^2 + bx + c &= (dx + e)(fx + g)",
                        r"\\ &= dfx^2 + dgx + efx + eg",
                        r"\\ &= dfx^2 + x(dg + ef) + eg"
                        ).to_corner(UL)
                

    equations2 = MathTex(r"a &= df", 
                   r"\\b &= dg + ef"
                   r"\\c &= eg").to_corner(LEFT)

    equations3 = MathTex(r"ax^2 + bx + c = dfx^2 + x(dg + ef) + eg",
                         r"ac = df \times eg = dg \times ef", 
                         r"\\b = dg + ef"
                         ).to_edge(UP)

    equations4 = MathTex(r"dfx^2 + x(dg + ef) + eg",
                         r" \\ dfx^2 + dgx + efx + eg",
                         r" \\ dx(fx + g) + e(fx + g)",
                         r" \\ (dx + e)(fx + g)"
                         )

    self.play(Write(intro))
    self.wait()
    
    self.clear()
    self.wait()

    for equation in equations1:
        self.play(Write(equation))
        self.wait()


    for equation in equations2:
      self.play(Write(equation))
      self.wait()

    self.clear()
    self.wait()

    n = 4

    for equation in equations3:
      self.play(Write((equation.center().shift(DOWN)).shift(UP * n)))
      self.wait()
      n -= 1

    n = 0

    for equation in equations4:
      self.play(Write(equation.center().shift(DOWN * n)))
      self.wait()
      n += 1
