word = "Donkey"

with open("file.txt", "r") as file:
    contents = file.read()
    contents = contents.replace(word, "######")

with open("file.txt", "w") as file:
    file.write(contents)