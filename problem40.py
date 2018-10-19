def concatenator(top_range):
    stringer = ""
    for idx, num in enumerate(range(1, top_range)):
        # print idx, num
        stringer += str(num)
        # print stringer
    return stringer


# concatenator(100)

def get_digit(target, stringer):
#     # print list(stringer)
    return list(stringer)[target-1]

# # 12th digit should be 1
# print get_digit(12, concatenator(100))
# # 11th digit should be 0
# print get_digit(11, concatenator(100))

temp_string = concatenator(10000000)
# print temp_string

print get_digit(1, temp_string)
print get_digit(10, temp_string)
print get_digit(100, temp_string)
print get_digit(1000, temp_string)
print get_digit(10000, temp_string)
print get_digit(100000, temp_string)
print get_digit(1000000, temp_string)

