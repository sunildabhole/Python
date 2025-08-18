with open("file.txt") as f:
    content1 = f.read()

with open("Poem.txt") as f:
    content2 = f.read() 

if (content1 == content2):
    print("Files are identical")

else:
    print("Files are different")