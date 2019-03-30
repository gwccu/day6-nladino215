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
while n <= 2 ** m:
    if n < 2 ** m:
        print(n)
        n *= n
    if n == 2 ** m:
        print(n)
        print("done")