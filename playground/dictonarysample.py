def sumfunc(a,b):
    """math sum operation"""
    return a+b

def multiply(a,b):
    """math multiply operation"""
    return a*b



#assign a function to a dictionary item
operations = {
    "+":sumfunc,
    "*":multiply
}

totaloperation=operations["*"]

print(totaloperation(2,5))

for _ in operations:
    print(_)