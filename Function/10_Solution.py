n = int(input("Enter any number find factorial: "))
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

print("factorial is =",factorial(n))