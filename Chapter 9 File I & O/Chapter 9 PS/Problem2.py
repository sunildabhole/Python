import random

def game():
    print("You are playing a guessing game!")
    score = random.randint(1, 62)   
    # Fetch the high score from a file
    with open("highscore.txt") as f:
        highscore = f.read()
        if (highscore != ""):
            highscore = int(highscore)
        else:
            highscore = 0

    print("Your score is:", score)
    if(score > highscore):
        # write the high score to a file
        with open("highscore.txt", "w") as f:
            f.write(str(score))
    
    return score

game()