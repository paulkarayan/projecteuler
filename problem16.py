#https://projecteuler.net/problem=16

def sumdigits(num):
    print(sum([int(char) for char in str(num)]))    



sumdigits(2**15)
sumdigits(2**1000)
