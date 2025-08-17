'''
sum(1) = 1
sum(2) = 1 + 2
sum(3) = 1 + 2 + 3
sum(4) = 1 + 2 + 3 + 4
sum(5) = 1 + 2 + 3 + 4 + 5
sum(n) = 1 + 2 + 3 + ... + n
sum(n) = sum(n-1) + n
'''


def sum(n):
    if n == 1:
        return 1
    else:
        return sum(n-1) + n

n = int(input("Enter a natural number: "))
print("Sum of first", n, "natural numbers:", sum(n))  # Example usage to calculate the sum