#https://discord.com/channels/581738731934056449/780234936980078602/950687828700979240
def numberToBase(n, b):
    if n == 0:
        return [0]
    digits = []
    while n:
        digits.append(int(n % b))
        n //= b
    return digits[::-1]
class opening_scene(Scene):
    def construct(self):
        one = Integer(9).scale(0.8)
        ten = Integer(9).next_to(one,LEFT).scale(0.8)
        rect_one = SurroundingRectangle(one,buff= 0.1)
        rect_ten = SurroundingRectangle(ten,buff = 0.1)
        self.play(Create(VGroup(one,ten)))
        self.wait()
        for i in range (99,99,-1):
            temp = numberToBase(i,10)
            self.play(  one.animate.set_value(temp[1]),
                        ten.animate.set_value(temp[0]),
                        run_time = 0.5
                    )
        self.wait(2)
        self.play(  Create(rect_one),
                    Create(rect_ten)
                )
        vertical_numbers = VGroup().move_to(one.get_center())
        for i in range(11):
            num_obj = Integer(i).scale(0.8)
            rect = SurroundingRectangle(num_obj,buff=0.1)
            num_obj.move_to(rect.center())
            vertical_numbers.add(VGroup(num_obj,rect)).arrange(DOWN)

        line_top = Line(start =rect_one.get_top(), end= vertical_numbers.get_top(),)
        line_bottom = Line(start =rect_one.get_bottom(), end= vertical_numbers.get_bottom() )
        

        self.play(  ReplacementTransform(VGroup(one,rect_one),vertical_numbers),   
                )
        self.wait()
        
        self.play(vertical_numbers.animate.shift(DOWN*0.8))
        self.wait()

        self.play(vertical_numbers.animate.shift(DOWN*2*0.8))
        self.wait()
        
        self.play(vertical_numbers.animate.shift(UP*4*0.8))
        self.wait()

        self.play(  ReplacementTransform(vertical_numbers,one.next_to(ten,RIGHT)),
                   
                 )
        self.wait()
