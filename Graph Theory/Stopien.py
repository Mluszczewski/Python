graf = {1: [3],
        2: [3, 5],
        3: [1, 2, 4, 5],
        4: [3],
        5: [3, 2],
        6: []
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


graph = add_krawedzie(graf)
print ("Podany graf:")
print graph

StopienGrafu = 0
for k, v in licz:
    print("Stopien wierzcholka nr: " + str(k) + " ="), len(v)
    if len(v) > StopienGrafu:
        StopienGrafu = len(v)

print("Stopien grafu = " + str(StopienGrafu))
