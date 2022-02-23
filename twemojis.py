temp = TexTemplate()
temp.add_to_preamble(r'\usepackage{twemojis}')
temp.add_to_preamble(r'\setlength\fboxrule{1sp}')
temp.add_to_preamble(r'\newcommand{\e}[1]{\fbox{\twemoji{#1}}}')

class WriteStuff(Scene):
    def construct(self):
        example_tex = MathTex(
            r'\e{cry}',
            r'+',
            r'\e{rofl}',
            r'=',
            r'\e{ok_hand} \e{sweat_drops}',
            tex_template=temp,
            font_size=144,
            color = None
        )
        example_tex.set_color_by_tex('+', WHITE)
        example_tex.set_color_by_tex('=', WHITE)
        
        self.play(Write(example_tex))
        self.wait()

#I also had to go to the twemoji's pdf-twemojis folder and run the following command to convert all the PDFs into EPS files which work better with the Manim pipeline:
# for i in *; pdftops -level3 -eps $i $i:r.eps
