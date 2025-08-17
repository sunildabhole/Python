import random
'''
1 for snake
-1 for water
0 for gun
'''
computer_choice = random.choice([1, -1, 0])
user_choice = int(input("Enter your choice (1 for snake, -1 for water, 0 for gun): "))

if user_choice == computer_choice:
    print("It's a tie!")
elif (user_choice == 1 and computer_choice == 0) or (user_choice == -1 and computer_choice == 1) or (user_choice == 0 and computer_choice == -1):
    print("You win!")
else:
    print("You lose!")