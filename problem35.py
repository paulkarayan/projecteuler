#circular primes

import math

examples_below_hundred = [2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, 97]

# check if circular prime
def is_circular_prime(prime_list, prime_candidate):
    if prime_candidate in prime_list:
        # print prime_candidate, "<---pc"
        rotated_list = rotate_digits(prime_candidate)
        # print rotated_list, "rl"
        for val in rotated_list:
            if int(val) not in prime_list:
                return False
        return True


def rotate_digits(input_value):
    #can be rotated len(input_value) - 1 times
    input_value = str(input_value)
    rotated = []
    for idx in list(input_value):
        temp = list(input_value)
        # print temp, type(temp)
        moved_val = temp.pop()
        # print moved_val, "<--mv"
        temp.insert(0, moved_val)
        # print temp, input_value, idx, moved_val
        input_value = ("").join(temp)
        # print input_value, "<--joined iv"
        rotated.append(input_value)

    # print rotated
    return rotated

# rotate_digits(197)

# # tester
# circ_primes = []
# for item in examples_below_hundred:
#     if is_circular_prime(examples_below_hundred, item):
#         print item, "<---circ prime yay!"
#         circ_primes.append(item)

# print circ_primes



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
            print(pos, "<--found prime")
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

# get all primes to limit
primes = []
sieve = []
counter = 10
while counter <= 100000000000:
    counter *= 10
    primes, limit, sieve = findprimes(counter, sieve, primes, 1000000)
    print(counter, "<=resized", primes, len(primes))

# should be 78498 per google search
million_primes = primes

circ_primes = []
for idx, item in enumerate(million_primes):
    if is_circular_prime(million_primes, item):
        print idx, item, "<---circ prime yay!"
        circ_primes.append(item)

print circ_primes
print len(circ_primes)