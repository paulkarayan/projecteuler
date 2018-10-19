# truncatable primes

import math

def findprimes(limit, sieve, plist, stop_length): # sieve of eratosthenes w/ tricks
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
            if len(p) >= stop_length:
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


def left_to_right_and_back(num, primes):
    values_to_test = [num, ]
    lister = list(str(num))
    for idx in list(str(num)):
        lister.pop()
        try:
            thing_to_test = int("".join(lister))
        except: 
            continue
        # print thing_to_test
        if not test_primes(thing_to_test, primes):
            return
        # values_to_test.append("".join(lister))
    
    lister = list(str(num))
    for idx in list(str(num)):
        del lister[0]
        # print lister
        try:
            thing_to_test = int("".join(lister))
        except: 
            continue
        if not test_primes(thing_to_test, primes):
            return
        # values_to_test.append("".join(lister))
    # print "huzzah", values_to_test
    return num

def test_primes(value_to_test, primes):
    if value_to_test not in primes:
        return False
    return True
    # print "huzzah", values_to_test

# 3797
# left_to_right_and_back(3797)


# get all primes to limit
primes = []
sieve = []
counter = 10
while counter <= 100000000000:
    counter *= 10
    primes, limit, sieve = findprimes(counter, sieve, primes, 1000000000)
    # print(counter, "<=resized", primes, len(primes))

# print left_to_right_and_back(3797, primes)

hits = 0

while hits <= 11:
    for prime in primes:
        # print prime, "<--- next"
        it = left_to_right_and_back(prime, primes)
        if it and it > 7:
            hits += 1
            print it

# 23
# 37
# 53
# 73
# 313
# 317
# 373
# 797
# 3137
# 3797
# 739397
