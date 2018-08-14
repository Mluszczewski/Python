class Graf():
    def __init__(self, wierzcholek):
        self.graf = Graf
        self.V = wierzcholek

    def check(self, v, pozycja, sciezka):
        if self.graf[sciezka[pozycja - 1]][v] == 0:
            return False

        for wierzcholek in sciezka:
            if wierzcholek == v:
                return False

        return True

    def Kolejka(self, sciezka, pozycja):
        if pozycja == self.V:
            if self.graf[sciezka[pozycja - 1]][sciezka[0]] == 1:
                return True
            else:
                return False

        for v in range(1, self.V):
            if self.check(v, pozycja, sciezka):
                sciezka[pozycja] = v
                if self.Kolejka(sciezka, pozycja + 1):
                    return True

                sciezka[pozycja] = -1
        return False

    def Hamilton(self):
        sciezka = [-1] * self.V
        sciezka[0] = 0

        if not self.Kolejka(sciezka, 1):
            print("Graf nie posiada cyklu Hamiltona")
            return False

        self.odp(sciezka)
        return True

    def odp(self, sciezka):
        print("Graf posiada cykl Hamiltiona :")
        for wierzcholek in sciezka:
            print wierzcholek,
        print sciezka[0]


g1 = Graf(5)
g1.graf = [[0, 1, 0, 1, 0],
           [1, 0, 1, 1, 1],
           [0, 1, 0, 0, 1],
           [1, 1, 0, 0, 1],
           [0, 1, 1, 1, 0]]
g1.Hamilton()

g2 = Graf(5)
g2.graf = [[0, 1, 0, 1, 0],
           [1, 0, 1, 1, 1],
           [0, 1, 0, 0, 1],
           [1, 1, 0, 0, 0],
           [0, 1, 1, 0, 0]]
g2.Hamilton()

g3 = Graf(8)
g3.graf = [[0, 0, 1, 0, 1, 0, 1, 0],
           [0, 0, 0, 0, 0, 0, 1, 0],
           [1, 0, 0, 0, 0, 1, 0, 0],
           [0, 0, 0, 0, 0, 1, 0, 0],
           [1, 0, 0, 0, 0, 0, 0, 1],
           [0, 0, 1, 1, 0, 0, 0, 0],
           [1, 1, 0, 0, 0, 0, 0, 0],
           [0, 0, 0, 0, 1, 0, 0, 0]]
g3.Hamilton()

g4 = Graf(4)
g4.graf = [[0, 1, 0, 0],
           [1, 0, 0, 0],
           [0, 0, 0, 1],
           [0, 0, 1, 0]]
g4.Hamilton()

g5 = Graf(5)
g5.graf = [[0, 1, 1, 1, 1],
           [1, 0, 1, 1, 1],
           [1, 1, 0, 1, 1],
           [1, 1, 1, 0, 1],
           [1, 1, 1, 1, 0]]
g5.Hamilton()
