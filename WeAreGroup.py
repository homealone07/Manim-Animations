#https://discord.com/channels/581738731934056449/780234936980078602/950452838386003968
def construct(self):
   
     t=Title("We are")
     b=BulletedList('Abhay','Aditi','Amogh','Amith','Sarath','Pradhyuman')
     b.set_color_by_tex("Abhay",RED)
     b.set_color_by_tex("Aditi",GREEN)
     b.set_color_by_tex("Amogh",BLUE)
     b.set_color_by_tex("Amith",BLUE)
     b.set_color_by_tex("Sarath",GREEN)
     b.set_color_by_tex("Pradhyuman",RED)

     self.play(Write(t))
     self.play(Write(b),run_time=6)
