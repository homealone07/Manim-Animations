def construct(self):
       graph = ImplicitFunction(
        lambda x, y:  np.cos(20*(np.arctan(2*(x-1)/y)+np.arctan(y/(x+1)))),
        min_depth=8,                 
    )
       self.play(Write(graph,run_time=6))
