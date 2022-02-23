from manim import *

class test(Scene):

    def construct(self):

        sd = Tex('Teorema de Pitágoras')
        sds = Tex('@nicolasiemini')

        self.play(
            Create(sd),
            run_time=2
        )

        self.play(
            Transform(
                sd,sds
            ),
            run_time=3
        )

        self.play(
            Unwrite(
                VGroup(
                    sd,sds
                )
            ),
            run_time=2
        )

        numberplane = NumberPlane()
        

        dota = Dot ([-2,2,0])
        dotb = Dot ([-2,-1,0])
        dotc = Dot ([3,-1,0]) 
        dote = Dot ([0,0,0])
        dotd = Dot ([0,-1,0])
        dotf = Dot ([-2,0,0])

        dotetxt = Tex('a').next_to(dote,UP*3+RIGHT*2)
        dotdtxt = Tex('b').next_to(dotd,DOWN)
        dotftxt = Tex('c').next_to(dotf,LEFT+UP*1.2)

  

        self.play(
            Create(dota),
            Create(dotb),
            Create(dotc), 
        )
        

        line_ab = Line(dota,dotb)   
        line_bc = Line(dotb,dotc) 
        line_ca = Line(dotc,dota)

       
        self.play(
            Create(line_bc),
            run_time = 0.5
        )
        self.play(
            Create(line_ca),
            run_time = 0.5
        )
        self.play(
            Create(line_ab),
            run_time = 0.5
        )

        self.play(
            Create(dotetxt),
            Create(dotdtxt),
            Create(dotftxt),
            run_time = 1.5
        )
        self.wait(1)

        formula = MathTex(r'a^2 = b^2 + c^2')
        formula.next_to(dotdtxt,DOWN)
        
        formula1 = MathTex(r'a = \sqrt{b^2 + c^2}').next_to(dotdtxt,DOWN)

        self.play(
            Create(formula),
            run_time = 1
        )
        
        self.wait(2)

        self.play(Transform(formula,formula1),run_time = 1.2)
        self.wait(1)

        numero = Tex(21).next_to(dotf,LEFT+UP*1.2)
        numero1 = Tex(28).next_to(dotd,DOWN)

        self.play(
        Transform(dotftxt,numero),
        Transform(dotdtxt,numero1),
        run_time = 1.2
        )
        self.wait(1)

        self.play(Unwrite(VGroup(formula,formula1)),run_time = 1.5)

        equação = MathTex(r'a = \sqrt{28^2 + 21^2}').next_to(dotdtxt,DOWN)

        self.play(
            Create(equação),
            run_time = 2
        )

        self.wait(1)

        resultado = MathTex(r'a = \sqrt{441 + 784}').next_to(dotdtxt,DOWN)

        self.play(
        Transform(equação,resultado),
        run_time = 1.2
        )

        self.wait(1)

        resultado1 = MathTex(r'a = \sqrt{1225}').next_to(dotdtxt,DOWN)

        self.play(Unwrite(VGroup(equação,resultado)),run_time = 1.5)

        self.play(
            Create(resultado1),
            run_time = 2
        )

        resultadofinal = MathTex(r'a = 35 ').next_to(dotdtxt,DOWN)

        self.play(
            Transform(resultado1,resultadofinal),
            run_time = 4
        )

        resultadoA =  Tex('35').next_to(dote,UP*3+RIGHT*2) 

        self.play(
            Transform(dotetxt,resultadoA),
            run_time = 2
        )




        self.wait(5)









    

    


     

        

    

 
