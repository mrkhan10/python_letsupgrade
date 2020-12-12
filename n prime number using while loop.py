#program to print  X prime numbers from 0 using while loop

x = int(input(" Please Enter Any Number: "))

Number = 1

print("Prime numbers between", 1, "and",x, "are:")

while(Number <= x):
    count = 0
    i = 2

    while(i <= Number//2):
        if(Number % i == 0):
            count = count + 1
            break
        i = i + 1

    if (count == 0 and Number != 1):
        print(" %d" %Number, end = '  ')
    Number = Number  + 1