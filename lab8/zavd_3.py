import random
n = int(input("n= "))
x = [0, 9, 9]
def el(x, n):
    for i in range(3, n):
        b = x[i-1] + 4 * x[i-3]
        x = x + [b]
    return(x)
x = el(x, n)
print("x[n]= {0}".format(x[n-1]))