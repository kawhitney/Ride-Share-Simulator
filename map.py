import networkx as nx
import matplotlib.pyplot as plt

class Map:
    '''

    '''
    def __init__(self, nodes, connectivity, seed):
        self.seed = seed
        self.graph = nx.gnp_random_graph(nodes, connectivity, seed=seed)
        self.color = 'lightblue'

    def change_color(self, color):
        self.color = color

    def display_graph(self): # needs work - does not show correctly
        pos = nx.spring_layout(self.graph, seed=self.seed, k=1.0)
        nx.draw_spring(self.graph, node_size=500, node_color=self.color, linewidths=0.25,
        font_size=10, font_weight='bold', with_labels=True)
        plt.show()