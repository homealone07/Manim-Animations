import networkx as nx
nxgraph = nx.erdos_renyi_graph(14, 0.5)

class ImportNetworkxGraph(Scene):
                def construct(self):
                    G = Graph.from_networkx(nxgraph, layout="spring", layout_scale=3.5)
                    self.play(Create(G))
                    self.play(*[G[v].animate.move_to(5*RIGHT*np.cos(ind/7 * PI) +
                                                     3*UP*np.sin(ind/7 * PI))
                                for ind, v in enumerate(G.vertices)])
                    self.play(Uncreate(G))
