# i think we only have to look up to 1/2 since that'll be last that divides cleanly

def sum_of_divisors(num):
    sod = [div for div in range(1, (num/2) + 1) if num % div == 0]
    # print sod, sum(sod)
    return sum(sod)

# 220 => 284, 284 => 220
sum_of_divisors(220)
sum_of_divisors(284)

results = {num: sum_of_divisors(num) for num in range(1,10000)}

# print results
print results[220], results[284]

amicables = list()
for k in results.keys():
    # print k
    # if k == 220 or k == 284:
    #     print results.get(k), results.get(results.get(k))
    if k == results.get(results.get(k)) and k != results.get(k) :
        print k, results.get(k), "amicable!"
        amicables.append(k)
print sum(amicables)
    