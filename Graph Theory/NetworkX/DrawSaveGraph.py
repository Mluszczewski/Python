import matplotlib.pyplot as plt
import networkx as nx


G = nx.Graph()
G.add_nodes_from([0, 1, 2, 3, 4, 5, 6, 7])

G.add_edges_from([(0, 1), (0, 4), (0, 5), (0, 7)])
G.add_edges_from([(1, 2), (1, 3), (1, 4), (1, 7)])
G.add_edges_from([(2, 6), (2, 3)])
G.add_edges_from([(4, 3), (4, 5), (4, 7), (7, 5)])


nx. write_edgelist(G, path="grid.edgelist", delimiter=":")
H = nx.read_edgelist(path="grid.edgelist", delimiter=":")

nx. write_adjlist(G, path="grid.adjlist", delimiter=":")
I = nx.read_adjlist(path="grid.adjlist", delimiter=":")


nx.draw(G)
plt.show()
