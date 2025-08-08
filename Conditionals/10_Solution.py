dog_age = int(input("Enter age of dog: "))
cat_age = int(input("Enter age of cat: "))

if dog_age <= 2:
    food = "Puppy Food"
else:
    food = "Adult dog Food"
print("Dog Food ->", food)
if cat_age <= 5:
    food = "Cat Food"
else:
    food = "Senior cat Food"
print("Cat Food ->", food)