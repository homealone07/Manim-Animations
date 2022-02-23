class TexTest(Scene):
  def construct(self):
    tex = MathTex(r"{ a \over {{b}} }=", r"{ {{x}} \over y}")
    self.play(Create(tex))
