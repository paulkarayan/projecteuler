


def genfibs():
    x,y = 1,2
    while 1:
        yield x
        x,y = y, x+y



def digit_finder(num_digits):
    
    counter = 1

    g = genfibs()
    while 1:
        x = next(g)
        counter += 1
        if len(str(x)) >= num_digits:
            print(x, len(str(x)), counter, "<---done")
            break
        

# 12th term should be 1st to contain 3 digits
digit_finder(3)

#answer here
digit_finder(1000)