#https://projecteuler.net/problem=15

from math import factorial

#observation is that this is just a combination, where we have x rights and
# x downs. so in the case of 20x20, this is recombining the ways we can go
# 20 down and 20 right

def combination(n,k):
    return factorial(n) / (factorial(k) * factorial(n-k))


print(combination(4,2))
print(combination(40,20))

# 137846528820


#here's another way to solve it from:
# http://code.jasonbhill.com/python/project-euler-problem-15/

#recursive solution. note how they stay from the base case and recurse.

import time
 
gridSize = [20,20]
 
def recPath(gridSize):
    """
    Recursive solution to grid problem. Input is a list of x,y moves remaining.
    """
    # base case, no moves left
    if gridSize == [0,0]: return 1
    # recursive calls
    paths = 0
    # move left when possible
    if gridSize[0] > 0:
        paths += recPath([gridSize[0]-1,gridSize[1]])
    # move down when possible
    if gridSize[1] > 0:
        paths += recPath([gridSize[0],gridSize[1]-1])
 
    return paths
 
start = time.time()
result = recPath(gridSize)

elapsed = time.time() - start
## 
print "result %s found in %s seconds" % (result, elapsed)


#alternatively, look at the number of paths to each endpoint. this is
#what i was working out on paper except done correctly :P
#you can discern the pattern from here...
