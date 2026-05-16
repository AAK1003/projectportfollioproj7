import random

def comparison(reference, guessed_number, points):
    if reference == guessed_number:
        points += 10
        print(f"Good Job! You guessed the right number. You guessed {guessed_number} and it is correct. You now have {points} points.")
    elif reference - guessed_number == 1 or guessed_number - reference == 1:
        points += 9
        print(f"Good work! You guessed {guessed_number} but the right answer was {reference}. You now have {points} points.")
    elif reference - guessed_number == 2 or guessed_number - reference == 2:
        points += 8
        print(f"Good work! You guessed {guessed_number} but the right answer was {reference}. You now have {points} points.")
    elif reference - guessed_number == 3 or guessed_number - reference ==3:
        points += 7
        print(f"Good work! You guessed {guessed_number} but the right answer was {reference}. You now have {points} points.")
    elif reference - guessed_number == 4 or guessed_number - reference == 4:
        points += 6
        print(f"Good work! You guessed {guessed_number} but the right answer was {reference}. You now have {points} points.")
    elif reference - guessed_number == 5 or guessed_number - reference == 5:
        points += 5
        print(f"Good work! You guessed {guessed_number} but the right answer was {reference}. You now have {points} points.")
    else:
        print(f"Oh no! You were more than 5 off! You guessed {guessed_number} ut it was actually {reference}. That causes you to gain no points for this round!")
    return points

keep_going = True
points= 0
print("Welcome to the Random Number Guessing Game! Here are the rules: \nThere is a random number that is made by this program, you will need to guess a number from 1-10 and you will be awarded points based on how close you are to the number. \nHere are the point values: \n10 points for getting it right \n9 for one off \n8 for 2 off \n7 for 3 off \n6 for 4 off \n5 for 5 off \nNo points if you are over 5 away.")
print("Get ready, the program is starting now...")
while keep_going == True:
    guessed_number = int(input("What is the number you are guessing? "))
    points = comparison(random.randint(1, 10), guessed_number, points)
    keep_going = input("Do you want to keep going or keep your score and leave(K or L)? ").lower()
    if keep_going == "k":
        keep_going = True
    else:
        keep_going = False
    if keep_going == False:
        print(f"Good Job! You did well! You finished with {points}!")
        break