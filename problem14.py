#https://projecteuler.net/problem=14

import timeit

## would be faster to push the length, starting num into a dict
## and then search the dict for the largest length

def collatz(n):
    seq = []
    seq.append(n)
    while n != 1:
        
        if n % 2 == 0:
            n = n/2
            seq.append(n)
            #print(n)
        else:
            n = 3*n+1
            seq.append(n)
            #print(n)
    #print(seq)
    return seq

def maxseq(seq, maxseqnum):
    if len(seq) > maxseqnum:
        maxseqnum = len(seq)
        print(seq[0], maxseqnum, "<-- increased")
    #print(len(seq))
    return maxseqnum


#collatz(13)

## maxseqnum = 0
##for x in range(1,1000000):
##    
##    maxseqnum = maxseq(collatz(x), maxseqnum)
##
##print("done")




def collatztwo(n, soldict):
    seq = []
    seq.append(n)
    while n != 1:
        
        if n % 2 == 0:
            n = n/2
            seq.append(n)
            #print(n)
        else:
            n = 3*n+1
            seq.append(n)
            #print(n)
    #print(seq, soldict)
    soldict[len(seq)] = seq[0]
    
    return soldict



def runner(limit):
    soldict = {}
    for x in range(1,limit):
        soldict = collatztwo(x, soldict)
    
    print(max(soldict, key=soldict.get), "<==max", soldict)


# soldict = {}
# for x in range(1,10):
#     soldict = collatztwo(x, soldict)

# print(max(soldict, key=soldict.get), soldict)

## just pull out the largest value 
runner(1000000)

# print(timeit.Timer(lambda:runner()).timeit(number=5))
