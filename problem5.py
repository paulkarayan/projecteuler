#https://projecteuler.net/problem=5


#2520 is the smallest number that can be divided by each of the numbers
#from 1 to 10 without any remainder.

#What is the smallest positive number that is evenly divisible by all
#of the numbers from 1 to 20?

#  2      3      5      7     11     13     17     19


def trydivide(inputnum, limit):
    dumbarray = [0] * limit
    dumbarray[0] = dumbarray[1] = 1
    for i in range(2,limit):
        if inputnum % i == 0: 
            dumbarray[i] = 1

    #print(inputnum, dumbarray, sum(dumbarray))

    if sum(dumbarray) == limit:
        return 0
    else:
        return 1



x = 2
while trydivide(x,10):
    x += 2

print(x)

x = 2520
while trydivide(x,20):
    x += 20

print(x)

