import time

t0 = time.time()
a = 20000000**20000000
t1 = time.time()
x = len(str(a))
t2 = time.time()

print "Time pow:", t1-t0, "Time len:", t2-t1, "x:", x
