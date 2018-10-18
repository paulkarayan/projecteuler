#https://projecteuler.net/problem=3

##The prime factors of 13195 are 5, 7, 13 and 29.
##What is the largest prime factor of the number 600851475143 ?

import math

listofprimes = [2, 3]

def primefactors(inputnum, listofprimes):

    quotient = inputnum

    for prime in listofprimes:
        while prime <= quotient:
            tempquotient, remainder = divmod(quotient, prime)
            print(prime, remainder, quotient)

            if remainder != 0:
                break
            else:
                quotient = tempquotient


def naiveprimefinder(inputnum, listofprimes):

    quotient = inputnum

    for prime in listofprimes:

        while prime <= quotient:
            tempquotient, remainder = divmod(quotient, prime)
            # print(prime, remainder, quotient)

            if remainder != 0:
                break
            else:
                quotient = tempquotient
                
    if remainder != 0:
        listofprimes.append(quotient)

    return(listofprimes)


# # test naive prime finder
# for x in range(2,100):
#    listofprimes = naiveprimefinder(x, listofprimes)
# print listofprimes


def findprimessmall(n): # sieve of eratosthenes
    
    #find primes less than n
    # create an array of all the values between 0 and limit
    p, sieve = [], [1] * n
    sieve[0] = sieve[1] = 0

    
    for pos in range(0, n):
        if sieve[pos] == 1:
        #it's prime so add it to list
            p.append(pos)
            print(pos, n, "<--found prime")

            x = 1
            #set all the multiples of prime to 0
            while x*pos < n:
                try:
                    sieve[(x*pos)] = 0
                    x += 1
                    #print(n, x, pos, x*pos, "<---success")
                except:
                    print(n, x, pos, x*pos, "<---fail")
                    break
                    
    #print("findprimes:", p)
    return(p)

def findprimes(n): # sieve of eratosthenes w/ tricks
    
    #find primes less than n
    # create an array of all the values between 0 and limit
    p, sieve = [], [1] * int(math.sqrt(n))
    sieve[0] = sieve[1] = 0

    
    for pos in range(0, int(math.sqrt(n))):
        if sieve[pos] == 1:
        #it's prime so add it to list
            p.append(pos)
            #print(pos, n, "<--found prime")

            x = 1
            #set all the multiples of prime to 0
            while x*pos < int(math.sqrt(n)):
                try:
                    sieve[(x*pos)] = 0
                    x += 1
                    #print(n, x, pos, x*pos, "<---success")
                except:
                    print(n, x, pos, x*pos, "<---fail")
                    break
                    
    #print("findprimes:", p)
    return(p)

## strategy: find all the primes below the specified number
##           then, do factorization with them.
# plist = findprimes(13195)
# print primefactors(13195, plist)


plist = findprimes(600851475143)
primefactors(600851475143, plist)
    
#test
##primefactors(1100, listofprimes)
##primefactors(36, listofprimes)
##primefactors(13195, listofprimes)
