with open("log.txt") as f:
    lines = f.readlines()

line_no = 1
for line in lines:
    if "Python" in line:
        print(f"Found Python on line {line_no}!")
        break
    line_no += 1

else:
    print("Python not found.")