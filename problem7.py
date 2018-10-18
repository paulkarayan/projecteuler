#https://projecteuler.net/problem=7

import math

def findprimes(limit, sieve, plist, primelen): # sieve of eratosthenes w/ tricks
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
    # find primes less than limit
    # create an array of all the values between 0 and limit
    
    for pos in range(0, int(math.sqrt(limit))):
        #print(pos)
        if sieve[pos] == 1:
        #it's prime so add it to list
            p.append(pos)
            # print(pos, "<--found prime")
            x = 1
            if len(p) >= primelen:
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
while len(primes) < 10001:
    counter *= 10
    primes, limit, sieve = findprimes(counter, sieve, primes, 10001)
    print(counter, "<=resized", primes, len(primes))

print("\n\n")
print(primes, limit, len(primes), "<--outer loop")
