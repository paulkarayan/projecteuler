#https://projecteuler.net/problem=2


import unittest

def genfibs():
    x,y = 1,2
    while 1:
        yield x
        x,y = y, x+y
    

def sumfibs(limit):
    
    summer = 0
    g = genfibs()
    while 1:
        x = next(g)
        if x > limit:
            break
        if x % 2 == 0:
            summer += x

    print(summer)

sumfibs(4000000)

