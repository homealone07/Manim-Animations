class TracePathTest(Scene):
    def construct(self):
        r = 15
        omega = 4
        phi = 0
        self.t = 0 #time
        self.a = np.array([r*np.sin(omega*self.t),0,0])
        self.v = np.array([-r/omega,0,0]) #initializing velocity
        self.x = np.array([0,0,0]) #initializing pos
        
        tip = Dot(np.array([0,0,0]),fill_opacity=1.0) #initial position
        arrow = always_redraw(lambda: Arrow(start=ORIGIN,
                        end=tip.get_center(),
                        color=WHITE,stroke_width=2.0,buff=0.0))
        
        self.play(FadeIn(arrow),FadeIn(tip))
        self.wait()
        
        def update_tip(tip, dt):
            self.a = np.array([r*np.sin(omega*self.t),0,0])
            self.v = self.v + self.a*dt
            self.x = self.x + self.v*dt
            tip.move_to(self.x) #dx
            self.t += dt
        
        tip.add_updater(update_tip)
        
        self.wait(10)
