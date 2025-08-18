f = open ("my_file.txt")
print(f.read())
f.close()

# The same can be written using the with statement like this:
with open("my_file.txt") as f:
    print(f.read())

# You don't have to explicitly close the file