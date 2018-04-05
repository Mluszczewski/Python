import string

# Uzytkownik podaje graf
V = raw_input("Podaj ilosc wierzcholkow: ")
E = raw_input("Podaj ilosc krawedzi: ")

Krawedzie = []

# Uzytkownik podaje sasiadow wierzcholkow
for k in range(1, string.atoi(V) + 1):
    x = raw_input("Podaj sasiadow wierzcholka nr. " + str(k) + ": ").split("\n")
    # Program tworzy liste polaczen wierzcholkow
    x[0] = x[0].split()
    if x[0]:
        x[0] = [int(i) for i in x[0]]
        Krawedzie.append(x[0])

print ("lista sadziedztwa: ")
print Krawedzie

# Obliczanie stopni wszystkich wierzcholkow oraz stopnia grafu
StopienGrafu = 0
for k in range(1, string.atoi(V) + 1):
    y = len(Krawedzie[k - 1])
    print ("Stopien wierzcholka dla wierzcholka nr. " + str(k) + " to: " + str(y))
    if y > StopienGrafu:
        StopienGrafu = y

print ("Stopien grafu jest rowny: " + str(StopienGrafu))