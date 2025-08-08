student = {
    1:"ram",
    2:"sham",
    3:"vikey"
}

print(student.items()) # display all key value pairs

print(student.keys()) # Print all keys

print(student.values()) # Print all values

student.update({1:"jam"}) # Update dictionary
print(student)

print(student.get(1)) # You print new key return none

print(student[1]) # You print new key return error