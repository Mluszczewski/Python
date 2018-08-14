import networkx as nx

G = nx.Graph()

G.add_nodes_from([0, 1, 2, 3, 4, 5, 6, 7])

G.add_edges_from([(0, 1), (0, 4), (0, 5), (0, 7)])
G.add_edges_from([(1, 2), (1, 3), (1, 4), (1, 7)])
G.add_edges_from([(2, 6), (2, 3)])
G.add_edges_from([(4, 3), (4, 5), (4, 7), (7, 5)])

Tree = nx.is_tree(G)
Kom = nx.is_connected(G)
Dwu = nx.is_bipartite(G)

try:
    nx.find_cycle(G)
except:
    pass

print list(nx.find_cycle(G))

print ('Czy graf jest drzewem : ' + str(Tree))
print ('Czy graf jest grafem pelnym : ' + str(Kom))
print ('Czy graf jest dwudzielny : ' + str(Dwu))
print ('Czy graf posiada cykl : ' + str(list(nx.find_cycle(G))))
