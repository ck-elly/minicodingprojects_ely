#ask user for their answer
userAnswer = input("User's Choice:")

#function for computer random choose
import random
gamesList = ["Rock", "Paper", "Scissors"]
def computerAnswer():
    global a
    a = (random.choice(gamesList))
    print("Computer's Choice:", a)

a = str(computerAnswer())
computerAnswer()
