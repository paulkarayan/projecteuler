#https://projecteuler.net/problem=9

import math
def rollthru(limit):
    for a in range(1, limit):
        for b in range(a,limit):
            if a+b == 1000 - (math.sqrt(a**2 + b**2)):
            
                c = (math.sqrt(a**2 + b**2))

                
                print(a,b,c)
                
                if addstothousand(a,b,c):
                    print("got 'em")
                    break

def addstothousand(a,b,c):
    return a+b+c == 1000


print(addstothousand(991, 8, 1))
print(addstothousand(991, 1, 1))

rollthru(1000)

