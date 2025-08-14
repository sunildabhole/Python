marks1 = int(input("Enter first marks:"))
marks2 = int(input("Enter second marks:"))
marks3 = int(input("Enter third marks:"))

# Calculate total percentage

total_percentage = (100*(marks1 + marks2 + marks3))/300

if(total_percentage>=40 and marks1>=33 and marks2>=33 and marks3>=33):
    print("You are Pass")

else:
    print("You are Failed,try again next year")
    
print("Your total percentage is=",total_percentage)