p1 = "make a lot of money" 
p2 = "buy now" 
p3 = "subscribe this"
p4 = "click this"

message = input("Enter your comment:")

if((message in p1) or (message in p2) or (message in p3) or (message or p4)):
    print("It is spam")

else:
    print("It is not spam")