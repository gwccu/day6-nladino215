# File name: problemSetDay6.py
num = 1
n = int(input("write a number"))
while num <= n:
    if num % 2 == 0:
        print("# is even")
        num += 1
    if num % 2 != 0:
        print("# is odd")
        num += 1
t = "*"
print(t)
while t != "****":
    if t != "****":
        t += "*"
        print(t)
