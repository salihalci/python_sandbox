import random


def generateRandNumber():
    return random.randint(1,100)

randNumber = generateRandNumber()
print(f"Guessed number is:{randNumber}")

executionCount=0

#create game loop for execution
isFound = False

while isFound == False:

    guessedNumber = int(input("Guess a number"))
    print(f"guessNumber is:{guessedNumber}")
    
    if guessedNumber == randNumber:
        print("You Win!")
        isFound=True
    elif executionCount !=5 and guessedNumber>randNumber:
        print("Guess  small number.")
    elif executionCount !=5 and guessedNumber<randNumber:
        print("Guess big number.")
    executionCount +=1

    if executionCount == 5 and isFound==False:
        print("Reched the trial limit. 5")
        isFound = True