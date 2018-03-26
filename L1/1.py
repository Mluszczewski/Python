a = 0
b = 1

print "pierwsza opcja:",(bool and [b] or [a])
print "druga opcja: ",(bool and [a] or [b])[0]


valLog = [None, True, False]
valA = [None, 1]
valB = [None, 2]

for v in valLog:
    for a in valA:
        for b in valB:
            x = (v and [a] or [b])[0]
            y = v and a or b
            z = a if v else b
            if not(x == y) or not(y == z):
                print "v:", v, "a:", a, "b:", b, x, y, z
