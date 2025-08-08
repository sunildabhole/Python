password = input("Enter Password: ")

length=len(password)

if length < 6:
    criteria = "Weak Password"
elif length <=10:
    criteria = "Medium Password"
else:
    criteria = "Strong Password"

print("This password type is ->",criteria)