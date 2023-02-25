
student_scores={
            "Harry":81,
            "Ron":78,
            "Hermonie":99,
            "Draco":81,
            "Nevile":62
        }

print("Hello!")

greetings={}

for keys in student_scores:
    if(student_scores[keys]>80):
        greetings[keys]="Pass"
    else:
        greetings[keys]="Fail"


for keys in greetings:
    print(f"{keys} pass status is {greetings[keys]}")
    



