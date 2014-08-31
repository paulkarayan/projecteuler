#https://projecteuler.net/problem=12

def f7(seq):
    seen = set()
    seen_add = seen.add
    return [ x for x in seq if not (x in seen or seen_add(x))]

def trianglegen():
    a,b = 1,2
    while 1:
        yield a
        a,b = a+b, b+1
    #return sum(x for x in range(n))
    
def findfactors(num):
    counter = 2
    array = [0] * (num + 1)
    array[num] = 1

    while num > counter:
        quotient, rem = divmod(num,counter)
        #print(counter, quotient, rem, num, type(rem))
        if rem == 0:
            array[counter] = array[quotient] = 1
        
        counter += 1
        
        if array[counter] == 1:
            #print(array)
            break

    return sum(array) 

def findfactorstwo(num):
    counter = 2
    min = num
    array = [num]

    while num > counter:
        quotient, rem = divmod(num,counter)
        #print(counter, quotient, rem, num, type(rem))
        if rem == 0:
            array.append(counter)
            array.append(quotient)
            min = quotient
        counter += 1
        
        if counter >= min:
            array = f7(array)
            #print(array)
            break

    return len(array)

##print(f7([6,6,4,5,7,8]))
##   
##print(findfactorstwo(36))

g = trianglegen()
summed = 0
maxsum = 0
while summed < 500:
    
    num = next(g)
    summed = findfactorstwo(num)
    if summed > maxsum:
        maxsum = summed
        print(num,maxsum)
print(num, summed)
    

