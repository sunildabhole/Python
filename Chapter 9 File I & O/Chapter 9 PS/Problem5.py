word = ["Donkey","bad"]

with open("file.txt", "r") as file:
    contents = file.read()


for w in word:
    contents = contents.replace(w, "#" * len(w))

with open("file.txt", "w") as file:
    file.write(contents)    