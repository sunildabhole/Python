str = input("Enter String to check 1st non-repeated character: ")

for char in str:
    if str.count(char) == 1:
        print("This char-> ",char)
        break