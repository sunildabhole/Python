items = ["apple", "banana", "orange", "apple", "mango"]

unique_item = set()

for i in items:
    if i in unique_item:
        print("Duplicate is found:" ,i)
        break
    unique_item.add(i)