# Factorial of number 5 using loop

num = int(input("Enter a number: "))

factorial = 1

if num < 0:
    print("Sorry, factorial does not exist for negative numbers")
else:
    for i in range(1, num + 1):
        factorial *= i
        print("Factorial of", num, "is", factorial)