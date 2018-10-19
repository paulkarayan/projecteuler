# digit factorials


from math import factorial

factorial_cache = {}

def single_tweak(number):
    temp_adder = list()
    for digit in list(str(number)):
        digit = int(digit)
        if digit not in factorial_cache.keys():
            fact = factorial(digit)
            factorial_cache[digit] = fact
        else:
            fact = factorial_cache[digit]
        temp_adder.append(fact)

    if sum(temp_adder) == number:
        print "success", temp_adder, number
        return True
    print number, sum(temp_adder) 
    return False

# test
single_tweak(145)

results = list()
# whats the upper limit here?
# per jason's code blog, set digits to 9 and see if they produce a similarly long
# value. so 99999999 = 8 x 9! which is a 7 digit number
for num in range(3, 1000000000):
    result = single_tweak(num)
    if result:
        results.append(num)

print results, "<-results!"
# 40730
# [145, 40585] <-results!