import matplotlib.pyplot as plt
import networkx as nx


G = nx.Graph()
G.add_nodes_from([0, 1, 2, 3])

G.add_edges_from([(0, 1)])
G.add_edges_from([(1, 0)])
G.add_edges_from([(2, 3)])
G.add_edges_from([(3, 2)])

nx.draw(G)
plt.show()