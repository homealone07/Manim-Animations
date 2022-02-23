#Using manimce opengl's zoom/3d feature 
class CountDown(Scene):
    def construct(self):
        color = [RED,WHITE,BLUE,PURPLE]
        maxim = 10
        self.camera.shift(13.5*IN)
        for i in range(maxim,0,-1):
            num = MathTex(i,opacity=100).scale(3).shift(3*i*IN).set_color(color[i%4])
            self.add(num)
        self.play(self.camera.animate.shift(3*maxim*IN),run_time=maxim,rate_func=lambda t: t)
