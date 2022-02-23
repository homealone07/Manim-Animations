from manim import *


class FootballField(Scene):
    def construct(self):
        Title = Tex(
            "Football Field", 
            font_size = 96
            )
        
        FieldWithGrass = Rectangle(
            height = 5, 
            width= 10, 
            )
        
        FieldGrass = ImageMobject("\\Users\\sheed\\Downloads\\T45_f_1.jpg")
        
        FieldGrass.width = 10
        FieldGrass.shift(RIGHT*0.01)
        
        BlackBorder = Rectangle(
            height = 1, 
            width = 10, 
            fill_color = BLACK, 
            fill_opacity = 1, 
            stroke_color = BLACK
            ).shift(UP*3)
        
        BlackBorder2 = Rectangle(
            height = 1, 
            width = 10, 
            fill_color = BLACK, 
            fill_opacity = 1, 
            stroke_color = BLACK
            ).shift(DOWN*3)
       
        OutlineOfField1 = Square(side_length = 5).shift(LEFT*2.5)
        
        OutlineOfField2 = Square(side_length = 5).shift(RIGHT*2.5)
        
        OutlineOfField3 = Circle(
            radius=1, 
            stroke_color = WHITE
            ) 
        
        OutlineOfField4 = Rectangle(
            height = 2.7358490566, 
            width = 1.73913043478
            ).shift(RIGHT*4.13)        
        
        OutlineOfField5 = Rectangle(
            height = 2.7358490566, 
            width = 1.73913043478
            ).shift(LEFT*4.13) 
        
        OutlineOfField6 = Rectangle(
            height = 1.32075471698, 
            width = 0.869565217391
            ).shift(RIGHT*4.55)
        
        OutlineOfField7 = Rectangle(
            height = 1.32075471698, 
            width = 0.869565217391
            ).shift(LEFT*4.55)
        
        OutlineOfField8 = Arc(
            radius = 0.6, 
            angle = PI
            ).rotate(angle = PI/2).shift(RIGHT*2.98 + DOWN*0.3)
        
        OutlineOfField9 = Arc(
            radius = 0.6, 
            angle = PI
            ).rotate(angle = -PI/2).shift(LEFT*2.98 + DOWN*0.3)
        
        OutlineOfField10 = Arc(
            radius = 0.3, 
            angle = PI/2
            ).shift(DOWN*2.5 + LEFT*5)
        
        OutlineOfField11 = Arc(
            radius = 0.3, 
            angle = -PI/2
            ).shift(UP*2.5 + LEFT*5)
        
        OutlineOfField12 = Arc(
            radius = 0.3, 
            angle = PI/2
            ).rotate(angle = PI/2).shift(DOWN*2.5 + RIGHT*4.7)
        
        OutlineOfField13 = Arc(
            radius = 0.3, 
            angle = -PI/2
            ).rotate(angle = -PI/2).shift(UP*2.5 + RIGHT*4.7)
        
        OutlineOfField14 = Rectangle(
            height = 0.66037735849, 
            width = 0.217391304348
            ).shift(RIGHT*5.1)
        
        OutlineOfField15 = Rectangle(
            height = 0.66037735849, 
            width = 0.217391304348
            ).shift(LEFT*5.1)
        
        OutlineOfField16 = Dot()
        
        FieldWithoutGrass = Rectangle(
            height = 5,
            width = 10,
            fill_color = GREEN,
            fill_opacity = 1
        )

        self.play(
            Write(Title), 
            run_time = 2,
            )

        self.play(FadeOut(Title))

        self.add(FieldGrass)
        
        self.play(
            Create(BlackBorder), 
            Create(BlackBorder2)
            )
        
        self.play(
            DrawBorderThenFill(FieldWithGrass), 
            run_time=2
            )
        
        self.play(
            Create(OutlineOfField1), 
            Create(OutlineOfField2), 
            Create(OutlineOfField3),
            Create(OutlineOfField4),
            Create(OutlineOfField5),
            Create(OutlineOfField6),
            Create(OutlineOfField7),
            Create(OutlineOfField8),
            Create(OutlineOfField9),
            Create(OutlineOfField10),
            Create(OutlineOfField11),
            Create(OutlineOfField12),
            Create(OutlineOfField13),
            Create(OutlineOfField14),
            Create(OutlineOfField15),
            Create(OutlineOfField16)
            )
        
        self.wait()
       
        self.play(
            FadeOut(OutlineOfField1), 
            FadeOut(OutlineOfField2), 
            FadeOut(OutlineOfField3),
            FadeOut(OutlineOfField4),
            FadeOut(OutlineOfField5),
            FadeOut(OutlineOfField6),
            FadeOut(OutlineOfField7),
            FadeOut(OutlineOfField8),
            FadeOut(OutlineOfField9),
            FadeOut(OutlineOfField10),
            FadeOut(OutlineOfField11),
            FadeOut(OutlineOfField12),
            FadeOut(OutlineOfField13),
            FadeOut(OutlineOfField14),
            FadeOut(OutlineOfField15),
            FadeOut(OutlineOfField16)
        )
        
        self.play(Create(FieldWithoutGrass))
        
        self.wait()
