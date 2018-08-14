graf1 = [[0, 0, 1, 1, 1, 1],  # Nie jest dwudzielny
         [0, 0, 1, 1, 1, 1],
         [1, 1, 0, 0, 1, 1],
         [1, 1, 0, 0, 1, 1],
         [1, 1, 1, 1, 0, 0],
         [1, 1, 1, 1, 0, 0]]

graf2 = [[0, 0, 0, 1, 1, 1, 1],  # Jest dwudzielny
         [0, 0, 0, 1, 1, 1, 1],
         [0, 0, 0, 1, 1, 1, 1],
         [1, 1, 1, 0, 0, 0, 0],
         [1, 1, 1, 0, 0, 0, 0],
         [1, 1, 1, 0, 0, 0, 0],
         [1, 1, 1, 0, 0, 0, 0],
         ]


def dwudzielny(graf, src=0):
    kolory = [-1 for i in range(0, len(graf))]
    kolory[src] = 1
    queue = [src]

    while queue:
        u = queue.pop()
        for v in range(0, len(graf)):
            if graf[u][v]:
                if kolory[u] > 0:
                    kolory[v] = 1 - kolory[u]
                    queue.append(v)
                elif graf[u][v] and kolory[u] == kolory[v]:
                    return "Graf nie jest dwudzielny"
    return "Graf jest dwudzielny"



print dwudzielny(graf1)
print dwudzielny(graf2)
