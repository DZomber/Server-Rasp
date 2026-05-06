def suma(a,b):
    return a+b
print(suma(3,4))
#print(3,4,5) # -> dara un error
def suma1(*args):
    total = 0
    for arg in args:
        total += arg
    return total
print(suma1(1,2,3,4,5))

def suma2(*args):
    return sum(args)
print(suma2(1,2,3,4,5))