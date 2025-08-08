score = int(input("Enter your Score: "))

if score >= 101:
    print("Please enter valide Score")
    exit()

if score>=90:
    grade = "A"

elif score>=80:
    grade = "B"

elif score>=70:
    grade = "C"

elif score>=60:
    grade = "D"

else:
    grade = "F"

print("Grade->",grade)