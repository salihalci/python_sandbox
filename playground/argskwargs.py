#default parameter passing

def my_function(a,b,c=0):
    print(a)
    print(b)
    print(c)

my_function(c=1,b=2,a=3)

def add(*args):
    print(type(args)) #tuple
    print(f"First element is {args[0]}")
    print(f"sum2 {sum(args)}")


add(2, 3)
add(2, 3, 4, 5)

print("------------------------")


def calculate(**kwargs): #returns dictionary
    print(kwargs)
    print(kwargs["name"])

    for key, value in kwargs.items():
        print(f"key is: {key} and value is value:{value} ")



calculate(name='Salih',number=5)



