with open("log.txt") as f:
    contents = f.read()

if "Python" in contents:
    print("Found Python!")
else:
    print("Python not found.")
