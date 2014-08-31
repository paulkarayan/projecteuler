#https://projecteuler.net/problem=6

def sumsquarediff(limit):

    #sum of squares
    ss1 = sum([i*i for i in range(1,limit+1)])
    
    print(sum([i*i for i in range(1,limit+1)]))

    
    #square of sum
    x = sum([i for i in range(1,limit+1)])
    print(x)
    print((x*x) - ss1)



sumsquarediff(10)
sumsquarediff(100)
