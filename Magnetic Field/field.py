def construct(self):
       graph = ImplicitFunction(
        lambda x, y:  np.cos(20*(np.arctan((x-1)/y)+np.arctan(y/(x+1)))),
        color=PURE_GREEN,
        min_depth=8,                 
    )
       self.play(Write(graph,run_time=6))
