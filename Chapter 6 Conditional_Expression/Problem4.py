n = int(input("Enter a number to check prime or not:"))

for i in range(2,n):
    if(n%i == 0):
        print("Number is not prime number")
        break
else:
    print("Number is prime number")