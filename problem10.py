#https://projecteuler.net/problem=10

##The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
#Find the sum of all the primes below two million.

import math

def findprimes(limit, sieve, plist, maxp): # sieve of eratosthenes w/ tricks
    #print(limit, sieve, plist, "inputs")
    if not plist:
        sieve = [1] * int(math.sqrt(limit))
        sieve[0] = sieve[1] = 0
        start = 0
    else:
    
        start = len(sieve)
        sieve = [1] * int(math.sqrt(limit) + len(sieve))
        sieve[0] = sieve[1] = 0
        
    p = []
    #find primes less than limit
    # create an array of all the values between 0 and limit
    
    for pos in range(0, int(math.sqrt(limit))):
        #print(pos)
        if sieve[pos] == 1:
        #it's prime so add it to list
            p.append(pos)
            #print(pos, n, "<--found prime")
            x = 1

            if pos >= maxp:
                print("hit the limit")
                return(p, limit, sieve)
            
            #set all the multiples of prime to 0
            while x*pos < int(math.sqrt(limit)):
                try:
                    sieve[(x*pos)] = 0
                    x += 1
                    #print(limit, x, pos, x*pos, "<---success")
                except:
                    #print(limit, x, pos, x*pos, "<---fail")
                    break
                
                    
    #print("findprimes:", p)
    return(p, limit, sieve)


primes = []
sieve = []
counter = 10
maxp = 2000000
# maxp = 10
limit = 10000
counter_ceiling = 100000000000000

while limit <= counter_ceiling:
    counter *= 10
    primes, limit, sieve = findprimes(counter, sieve, primes, maxp)
    print(counter, "<=resized", primes)

    if primes[-1] >= maxp:
        break

print(primes, limit, len(primes), "<--outer loop")

print sum(primes)

## !!! then i manually subtracted off the last value - 2000003
