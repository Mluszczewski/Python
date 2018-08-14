import matplotlib.pyplot as plt
import networkx as nx


G = nx.Graph()
G.add_nodes_from([0, 1, 2, 3, 4, 5, 6, 7])

G.add_edges_from([(0, 2), (0, 4), (0, 6)])
G.add_edges_from([(1, 6)])
G.add_edges_from([(2, 0), (2, 5)])
G.add_edges_from([(3, 5)])
G.add_edges_from([(4, 0), (4, 7)])
G.add_edges_from([(5, 2), (5, 3)])
G.add_edges_from([(6, 0), (6, 1)])
G.add_edges_from([(7, 4)])

nx.draw(G)
plt.show()