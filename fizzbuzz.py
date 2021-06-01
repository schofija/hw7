def genNum():
    for i in range (1, 100):
        print(printNum(i))
    

def printNum(num):

    if num % 3 == 0:
        return("fizz")

    return(num)
    