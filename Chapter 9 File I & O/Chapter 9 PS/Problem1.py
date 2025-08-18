f = open("Poem.txt")
content = f.read()
if "twinkel" in content:
    print("Found 'twinkel' in the poem.")
else:
    print("Did not find 'twinkel' in the poem.")
f.close()