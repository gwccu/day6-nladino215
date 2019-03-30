# File name: warmupDay6.py
mynum = 2
guess = int(input("Guess a number"))
while guess != mynum:
    if guess != mynum:
        print("try again")
        guess = int(input("Guess a number"))
    if guess == mynum:
        print("You got it!")
print("good job!")

n = 2
m = 3
print(n ** m)

n = 2
m = 3
while n < 8:
    if n < 8:
        print(n)
        n *= 2
print(n)
