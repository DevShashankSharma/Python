def avg():
    n1 = int(input("Enter first number: "))
    n2 = int(input("Enter second number: "))

    print("The average of {0} and {1} is {2}".format(n1, n2, (n1 + n2) / 2))


avg()



def factorial(n):
    if n<0:
        return -1
    elif n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)


#! use of round function

n = int(input("Enter a number: "))

print("The factorial of {0} is {1}".format(n, round(factorial(n), 2)))