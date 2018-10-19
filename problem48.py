sub_list = []
for num in range(1,10):
    sub_list.append(num**num % 100000000000)
print sub_list
print sum(sub_list)
# 10405071317 is answer shown
# so with mod, it'll be 0405071317 <== last 10 digits


sub_list = []
for num in range(1,1000):
    sub_list.append(num**num % 100000000000)
print sub_list
print sum(sub_list)
# 145419110846700
# last 10 are 9110846700