import matplotlib.pyplot as plt
import networkx as nx

I = nx.read_gpickle(path="graphTests/test.gpickle")

D = nx.complement(I)
nx.draw(D)
#plt.show(D)


K = nx.line_graph(I)
nx.draw(K)
#plt.show(K)