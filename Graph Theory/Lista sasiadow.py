graf = {1: [2, 3, 5],
        2: [1, 3, 4],
        3: [1, 2],
        4: [2, 5],
        5: [4, 1]
        }

licz = graf.items()

def add_krawedzie(graph):
    krawedzie = []
    for punkt in graph:
        for sasiad in graph[punkt]:
            if sasiad not in graph.keys():
                return False
            elif graph.values() < 0:
                return False
            else:
                krawedzie.append((punkt, sasiad))

    return krawedzie

print ("Podany graf:")
print list(add_krawedzie(graf))

print "lista sasiadow dla poszczegolnych wierzcholkow:"
for v, k in graf.items():
    print list((v,k))
