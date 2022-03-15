#https://discord.com/channels/581738731934056449/582403919754297363/952564125991579698
from manim import *

class LandArea(Scene):
    def construct(self):
        #1
        landAreaBlock = Rectangle(width=2,height=2)
        landAreaText = Text("  Land Area\n Comparator", font_size= 20).move_to(landAreaBlock)
        landAreaGroup = VGroup(landAreaBlock,landAreaText)
        #2
        Input1Block = Rectangle(width=1.5,height=0.75)
        Input1Text = Text("Input", font_size= 20).move_to(Input1Block)
        Input1Group = VGroup(Input1Block,Input1Text).shift(LEFT*3+UP*0.5)
        #3
        Input2Block = Rectangle(width=1.5,height=0.75)
        Input2Text = Text("Input", font_size= 20).move_to(Input2Block)
        Input2Group = VGroup(Input2Block,Input2Text).shift(LEFT*3+DOWN*0.5)
        #4
        outputBlock = Rectangle(width=5.5,height=0.75)
        outputText = Text("Input[1] is NUMBER bigger than Input[2]", font_size= 20).move_to(outputBlock)
        outputGroup = VGroup(outputBlock,outputText).shift(RIGHT*4.5)
        
        arrow1 = Line(start= Input1Group.get_right(), end=landAreaGroup.get_left(), tip_length=0.1).add_tip()
        arrow2 = Line(start= Input2Group.get_right(), end=landAreaGroup.get_left(), tip_length=0.1).add_tip()
        arrow3 = Line(start= landAreaGroup.get_right(), end=outputGroup.get_left(), tip_length=0.1).add_tip()
        
        #5
        allInOne = Group(landAreaGroup,Input1Group,Input2Group,outputGroup,arrow1,arrow2,arrow3).shift(LEFT*1)
        
        self.play(Create(landAreaGroup))
        self.wait(1)
        self.play(FadeIn(Input1Group),FadeIn(Input2Group))
        self.wait(1)
        
        self.play(Create(arrow1),Create(arrow2))
        self.play(Create(arrow3),FadeIn(outputGroup))
