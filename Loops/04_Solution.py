string = input("Enter String to make reverse: ")
reverse_str = ""

for char in string:
    reverse_str = char + reverse_str
print("Reverse String is-> ",reverse_str)