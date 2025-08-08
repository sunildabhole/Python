n = int(input("Enter last number of calculate even numbers: "))
count_even = 0

for i in range(1,n+1):
    if i % 2 == 0 :
        count_even = count_even + 1
        # count_even += 1
print("Number of calculate even numbers is-> ",count_even)