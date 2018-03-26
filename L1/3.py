import time
import math

t0 = time.time()
x = 1234500 ** 123456
t1 = time.time()
xLen = len(str(x))
t2 = time.time()

print "Time pow:", t1 - t0, "Time len:", t2 - t1, "Len:", xLen

t0 = time.time()
x = 1234500 ** 123456
t1 = time.time()
xLen=int(math.ceil(math.log(x,10)))

t2 = time.time()

print "Time pow:", t1 - t0, "Time len:", t2 - t1, "Len:", xLen
