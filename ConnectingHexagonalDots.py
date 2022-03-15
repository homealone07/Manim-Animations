#https://discord.com/channels/581738731934056449/780234936980078602/950799148632915999
from manim import *


class MovingGraph(Scene):
    def construct(self):
        
        V = VGroup() # вершины графа
        E = VGroup() # ребра графа

        # Создаем вершины графа
        for i in range(6):
            vertex = Dot(3*RIGHT)
            vertex.rotate(TAU * (i/6), about_point=ORIGIN)
            V.add(vertex)

        # создаем ребра полного графа
        # добавляем апдейтер через always_redraw
        for i in range(6):
            for j in range(6):
                if i < j:                    
                    edge = always_redraw(
                        lambda i=i, j=j:
                        Line(V[i].get_center(),
                             V[j].get_center(),
                             stroke_width=2)
                        )
                    E.add(edge)    
        
        # Анимация
        self.play(Write(V), run_time=2)
        self.play(Write(E), run_time=4)

        self.play(ApplyMethod(V[0].shift, RIGHT),
            ApplyMethod(V[3].shift, LEFT))
        self.play(ApplyMethod(V[1].shift, 3*LEFT),
            ApplyMethod(V[2].shift, 3*RIGHT))
        self.play(ApplyMethod(V[5].shift, 3*LEFT),
            ApplyMethod(V[4].shift, 3*RIGHT))
        self.play(ApplyMethod(V[0].shift, -RIGHT),
            ApplyMethod(V[3].shift, -LEFT))

        self.wait(3)
