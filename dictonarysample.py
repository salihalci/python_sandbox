def sumfunc(a,b):
    return a+b


operations = {
    "*":sumfunc
}

totaloperation=operations["*"]

print(totaloperation(2,5))