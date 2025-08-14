# for loop with break
m = [1,2,3,4,5,6,7,8]

for i in m:
    if(i==4):
        break # Exit the loop right now
    print(i)


# for loop with continue
n = [1,2,3,4,5,6,7,8]
for i in n:
    if(i==7):
        continue # Skip this iteration
    print(i)