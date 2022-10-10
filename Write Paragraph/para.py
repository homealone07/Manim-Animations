class TestR(Scene):
    def construct(self):
        paragraph = Tex("""{5cm}
                                Lorem Ipsum is simply dummy text of the printing and typesetting industry. 
                                Lorem Ipsum has been the industry's standard dummy text ever since the 1500s,
                                when an unknown printer took a galley of type and scrambled it to make a 
                                type specimen book. It has survived not only five centuries, but also the leap
                                into electronic typesetting, remaining essentially unchanged. It was popularised 
                                in the 1960s with the release of Letraset sheets containing Lorem Ipsum 
                                passages, and more recently with desktop publishing software like Aldus
                                PageMaker including versions of Lorem Ipsum.""",
                              font_size=22,
                              tex_environment='minipage')

        self.play(Write(paragraph))
        self.wait(duration=4)
