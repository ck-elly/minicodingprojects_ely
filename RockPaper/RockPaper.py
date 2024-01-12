
#ask user for their answer
userAnswer = input("User's Choice: ")
#set userAnswer as str and into c
c = str(userAnswer)

#assign variables to each answer
x = "Rock"
y = "Paper"
z = "Scissors"

#declare function for computer random choose, not yet print
import random
gamesList = (x, z, y)
def computerAnswer():
    global a
    global b
    #set a as a the randomizer as a string
    a = str((random.choice(gamesList)))
    #combine the random answer with the text"computer's choice
    b = "Computer's Choice: " + a
#run the function    
computerAnswer()

#print the output
print(b)


#if there's a tie, loop
while a.lower() == c.lower():
    #ask user for their answer
    print("Tie! Try Again")
    userAnswer = input("User's Choice: ")
    #set userAnswer as str and into c
    c = str(userAnswer)

    #declare function for computer random choose, not yet print
    def computerAnswer():
        global a
        global b
        #set a as a the randomizer as a string
        a = str((random.choice(gamesList)))
        #combine the random answer with the text"computer's choice
        b = "Computer's Choice: " + a
       
    #run the function    
    computerAnswer()

    #print the output
    print(b)
    

#assign the final output to a variable
g = "You won babe :>"   
h = "You lost it babe :<"

#set every variable into lower-case
a = a.lower()
c = c.lower()
z = z.lower()
x = x.lower()
y = y.lower()

#won or not
if (c == x and a == z) or (c == y and a == x) or (c == z and a == y):
    print(g) 
else:
    print(h)

    