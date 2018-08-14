graf = {1: [2, 3, 5],
        2: [1, 3, 4],
        3: [1, 2],
        4: [2, 5],
        5: [4, 1]
        }


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


def dfs(graf, s):
    Stos = set()
    kolejka = []
    kolejka.append(s)
    while kolejka:
        u = kolejka.pop()
        if u in Stos: continue
        Stos.add(u)
        kolejka.extend(graf[u])
        yield u


print "DFS:"
print list(dfs(graf, 1))

print ("Podany graf:")
print list(add_krawedzie(graf))
