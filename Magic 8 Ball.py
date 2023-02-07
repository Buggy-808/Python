import random, time

question = input("To ask the Magic 8 Ball a question press ENTER")
time.sleep(5)
print("Searching for an answer")
time.sleep(1)
print("Please be patient")

for i in range(10):
    print(".")
    time.sleep(.5)

time.sleep(1)
answer = random.randint(1,9)

if answer == 1:
    print("All signs point to yes")

elif answer == 2:
    print("It is unknown")

elif answer == 3:
    print("Yes, yes, yes")

elif answer == 4:
    print("My sources say no")

elif answer == 5:
    print("My sources say yes")

elif answer == 6:
    print("Most definitely")

elif answer == 7:
    print("My sources are undetermined")

elif answer == 8:
    print("No, no, no")

elif answer == 9:
    print("Ask again later")
    
