#https://projecteuler.net/problem=4


#A palindromic number reads the same both ways.
#The largest palindrome made from the product of two 2-digit numbers
#is 9009 = 91 × 99.

#Find the largest palindrome made from the product of two 3-digit numbers.


def ispalindromidary(num):
    num = list(map(int, str(num)))

    revnum = num[::-1]
    
    #print(num, revnum)

    if revnum == num:
        return 1
    else:
        return 0


#test
print(ispalindromidary(99))
print(ispalindromidary(19240522))


def rollthru(n,s):
    dumblist=[]
    x = [x for x in range(100,n+1)][::-1]
    y = [x for x in range(100,s+1)][::-1]

    print(x,y)
    counter = 1
    for l in x:
        counter += 1
        
        for m in y[:counter]:
         
            #print(l,m,l*m, ispalindromidary(l*m))

            if ispalindromidary(l*m):
                print("hooray, it's:", ispalindromidary(l*m))
                dumblist.append(l*m)
                
    return dumblist
    
nlist = rollthru(999,999)
print(nlist)

print(nlist.sort())
