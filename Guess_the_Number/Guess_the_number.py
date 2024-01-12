#declare a function for choosing a random number
def randomNumber():
    import random
    global i
    i = (random.randrange(1,10))

#run the declared function
randomNumber()

#ask the user for their guessed number    
ii = (input("What's your guess? "))
ii = (int(ii))

#keep asking if the guessed number does not match the actual number
while ii != i:
    if ii > i:
        ii = (int(input("Lower! ")))
    if ii < i:
        ii =(int(input("Higher! ")))
    if ii == i:
        print("You guessed it babe")
        break

    

      