graf = {1: [2, 3],  # Graf eulerowski
        2: [3, 1],
        3: [1, 2]
        }

graf1 = {1: [2, 3, 4],  # Graf poleulerowski
         2: [3, 1],
         3: [1, 2],
         4: [1]
         }

graf2 = {1: [2, 3, 4],  # To nie jest graf eulerowski
         2: [1],
         3: [1],
         4: [1]
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


def nieparzysty(n):
    return n % 2 == 1


def Euler(graf):
    lista = []
    for wierzcholek, sasiad in graf.items():

        if nieparzysty(len(sasiad)):
            lista.append(wierzcholek)

    if len(lista) == 0:
        return "Graf jest spojny i eulerowski"
    elif len(lista) == 2:
        return "Graf 1 jest spojny i poleulerowski"
    else:
        return "Graf 2 nie jest spojny i eulerowski"


print Euler(graf)
print "***********************************"
print Euler(graf1)
print "***********************************"
print Euler(graf2)
print "***********************************"

print ("Podany graf:")
print list(add_krawedzie(graf))
