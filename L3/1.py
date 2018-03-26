

"""
print [z ** 2 for z in range (10) if z % 2 == 0]
print [z ** 2 for z in range (10) if z % 2 != 0]
"""


"""
vec = [2, 4 ,6]
print [3*x for x in vec]
print [3*x for x in vec if x > 3]
print [3*x for x in vec if x < 2]
print [[x, x**2] for x in vec]
print [(x, x**2) for x in vec]
print [[x, x**2, x+2, x-2, x/2, x%2] for x in vec]
"""


"""
vec1 = [2,4,6]
vec2 = [4,3,-9]
print [x*y for x in vec1 for y in vec2]
print [x+y for x in vec1 for y in vec2]
print [vec1[i]*vec2[i] for i in range(len(vec1))]
"""


"""
print (1,2,3) < (1,2,4)
print [1,2.3] <[1,2,4]
print 'ABC' < 'C' < 'Pascal' < 'Python'
print (1,2,3,4) < (1,2,4)
print (1,2) < (1,2,-1)
print (1,2,3) == (1.0, 2.0, 3.0)
print (1,2, ('aa', 'ab')) < (1,2, ('abc', 'a'), 4)
"""
