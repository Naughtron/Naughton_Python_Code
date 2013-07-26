def dice():
        print "Welcome!"
 # import random into the function
import random
 
#set values of the die
min_side = 1
max_side = 20
 
# ask the user if they want to play
roll_the_die = raw_input("Want to hit a Beholder?: ")
 
# Beholders AC: 20
#create a while loop that will run so long as the users choice is y or yes
while roll_the_die == "y" or roll_the_die == "yes":
 
        # roll the d20
        d20 = random.randint(min_side, max_side)
       
        if d20 == 20: # if roll is a 20
                print "Natural 20!!!"
                print "Thats what it takes to hit this thing!"
                print "You rolled a %d " % d20
       
        elif d20 <= 19 and d20 > 12: # if roll is <= 19 and >12
                print "Miss"
                print "You rolled a %d " % d20
       
        elif d20 <= 12 and d20 > 10: # if roll is <= 12 and > 10
                print "Miss!"
                print "The Beholder just floats there, laughing at you."
                print "You rolled a %d " % d20
       
        elif d20 <= 5:
                print "Critical Miss!"
                print "The Beholder eats your face!"
                print "You rolled a %d " % d20
               
       
                # ask the user if they want to roll again
                roll_the_die = raw_input("Roll again?: ")