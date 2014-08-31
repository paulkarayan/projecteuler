#https://projecteuler.net/problem=1
#If we list all the natural numbers below 10 that are
#multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
#Find the sum of all the multiples of 3 or 5 below 1000.

#natural numbers: counting numbers, may or may not include 0

import unittest
def sumthreefive(end):
    counter = 0

    for x in range(0,end):
        if x % 3 == 0:
            counter += x
            continue
        
        if x % 5 == 0:
            counter += x 

    print(counter)
    return(counter)


#tests
class MyTest(unittest.TestCase):
    def test(self):
        self.assertEqual(sumthreefive(10), 23, "didn't add up")

if __name__ == '__main__':
    sumthreefive(1000)
    unittest.main()

    
