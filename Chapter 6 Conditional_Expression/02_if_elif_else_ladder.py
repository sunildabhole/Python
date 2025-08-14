age = int(input("Enter age:"))

if(age>=18):
    print("You are above the age of consent")
    print("Good For You")
    
elif(age<0):
    print("You entering an invalid nagative age")

elif(age==0):
    print("You enter zero which is not valid age")

else:
    print("You are below the age of consent")