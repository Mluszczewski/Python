import time
import random
import math
"""
def is_prime(num):
    for j in range (2, int(math.sqrt(num))+ 1):
        if (num % j) == 0:
            return False
"""

start1 = time.time()

def euk(a,b):
    while b != 0:
        a,b = b, a%b
    return a
print euk(50,20)

stop1 = time.time()
print 'Time1:', stop1 - start1

"""
lista = [16,4,8]
big1 = random.getrandbits(256)
big2 = random.getrandbits(256)
fst = 1000000000L
snd = 1000010000L
big3 = filter(is_prime, range(fst,snd))
print len(big3)

prime = 0
if big3:
    prime = big3[0]
else:
    prime = 997
print big1,big2,prime

start = time.time()
print euk(prime * prime, prime * prime * prime)
stop = time.time()
print 'Time:', stop - start
"""
