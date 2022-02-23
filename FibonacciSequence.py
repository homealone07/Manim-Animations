from manim import *

class Fib(Scene):
    def create_slots(self):
        b = Square()
        a = Square().next_to(b, direction=LEFT)
        c = Square().next_to(b, direction=RIGHT)
        
        self.play(AnimationGroup(Create(a), Create(b), Create(c), lag_ratio=0.2))
        
        plus = Text('+').next_to(b, direction=LEFT)
        equals = Text('=').next_to(b, direction=RIGHT)
        
        self.play(a.animate.next_to(plus, direction=LEFT), c.animate.next_to(equals), direction=RIGHT)
        self.play(AnimationGroup(Create(plus), Create(equals), c.animate.set_color('#FFEE00'), lag_ratio=0.1))
        
        self.asq = a
        self.bsq = b
        self.csq = c
        
    def construct(self):
        self.create_slots()
        
        a = 1
        b = 0
        c = 1
        
        at = Integer(number=a).move_to(self.asq)
        bt = Integer(number=b).move_to(self.bsq)
        ct = Integer(number=c).move_to(self.csq)
        
        self.play(AnimationGroup(Create(at), Create(bt), Create(ct), lag_ratio=0.1))
        
        while c < 1000:
            a = b
            b = c
            c = a + b
            
            self.play(
                at.animate.next_to(self.asq, direction=LEFT),
                bt.animate.move_to(self.asq),
                ct.animate.move_to(self.bsq)
            )
            
            a_out = FadeOut(at)
            
            at = bt
            bt = ct
            
            ct = Integer(number=c).move_to(self.csq)
            
            self.play(
                a_out,
                ReplacementTransform(Group(at.copy(), bt.copy()), ct)
            )
