try:
    with open("1.txt", "r") as f:
        print(f.read())
except Exception as e:
    print(e)
try:
    with open("2.txt", "r") as f:
        print(f.read()) 
except Exception as e:
    print(e)

try:
    with open("३.txt", "r") as f:
        print(f.read()) 
except Exception as e:
    print(e)

print("Thanks You!!")