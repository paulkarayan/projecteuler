#https://projecteuler.net/problem=16

number_dict = {
    0: "",
    1: "one", 2: "two", 3: "three", 4: "four", 5: "five", 
    6: "six", 7: "seven", 8: "eight", 9: "nine",
    10: "ten",
    11: "eleven",
    12: "twelve",
    13: "thirteen",
    14: "fourteen",
    15: "fifteen",
    16: "sixteen",
    17: "seventeen",
    18: "eighteen",
    19: "nineteen",
    20: "twenty",
    30: "thirty",
    40: "forty",
    50: "fifty",
    60: "sixty",
    70: "seventy",
    80: "eighty",
    90: "ninety",
    1000: "one thousand"
}


def string_length_finder(num):
    counter = 0
    for char in num:
        if str(char).isalpha():
            counter += 1
    return counter

## Quick Maffs - work out the nonstandard numbers
print sum(string_length_finder(num) for num in number_dict.values())


# convert numbers to written out in words form
def numberizer(input_value):
    string_builder = ""
    # get value of largest digit
    print str(input_value)[0]
    string_builder += number_dict[int(str(input_value)[0])] 
    string_builder += "hundred"

    if input_value % 10 == 0:
        print "divide by 10"
        return string_builder
    string_builder += "and"
    
    if str(input_value)[1] == 1 and str(input_value)[2] != 0:
        string_builder += number_dict[str(input_value)[1] + str(input_value)[2]]
        return string_builder

    print number_dict[int(str(input_value)[1] + "0")]
    string_builder += number_dict[int(str(input_value)[1] + "0")] 

    if int(str(input_value)[2]) != 0:
        string_builder += number_dict[int(str(input_value)[2])]

    return string_builder


# 342 (three hundred and forty-two) contains 23 letters and 
# 115 (one hundred and fifteen) contains 20 letters.
## test cases
assert string_length_finder("three hundred and forty-two") == 23
assert string_length_finder("one hundred and fifteen") == 20

print numberizer(342)
print numberizer(115)
print numberizer(110)
print numberizer(540)
print numberizer(600)
print numberizer(601)
