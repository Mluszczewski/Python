import networkx as nx

G = nx.Graph()

G.add_nodes_from([0, 1, 2, 3, 4, 5, 6, 7])

G.add_edges_from([(0, 1), (0, 4), (0, 5), (0, 7)])
G.add_edges_from([(1, 2), (1, 3), (1, 4), (1, 7)])
G.add_edges_from([(2, 6), (2, 3)])
G.add_edges_from([(4, 3), (4, 5), (4, 7), (7, 5)])

degrees = dict(nx.degree(G))
nodes = nx.number_of_nodes(G)
edges = nx.number_of_edges(G)
leafs = [x for x in G.nodes() if G.degree[x] == 1]
degree = [x for x in G.nodes() if G.degree[x] == 3]

print ('Stopien wierzcholkow wynosi :' + str(degrees))
print ('Graf posiada ' + str(nodes) + ' wierzcholkow ')
print ('Graf posiada ' + str(edges) + ' krawiedzi ')
print ('Ilosc lisci : ' + str(len(leafs)))
print ('Ilosc wierzcholkow o stopniu 3 : ' + str(len(degree)))
