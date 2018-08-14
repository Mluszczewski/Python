import matplotlib.pyplot as plt
import networkx as nx


G = nx.Graph()
G.add_nodes_from([0, 1, 2, 3, 4])

G.add_edges_from([(0, 1), (0, 2), (0, 3), (0, 4)])
G.add_edges_from([(1, 0), (1, 2), (1, 3), (1, 4)])
G.add_edges_from([(3, 0), (3, 1), (3, 2), (3, 4)])
G.add_edges_from([(4, 0), (4, 1), (4, 2), (4, 3)])

nx.draw(G)
plt.show()