# this version add comuter as player1 and random pick 1 or 2 sticks 
# play until you or computer will win

import random
    
sticks = int(input("How many sticks (N) in the pile: ")) # first know all sticks in the pile   
print("There are", sticks,"sticks in the pile.") 
name = str(input("What is your name: ")) # ask player name

# built function for check that player play follow the rule or not        
def player2(n,sticks): 
    # have 4 conditions to check 
    if n > 2: # player can take only 1 or 2 sticks 
        print("No you cannot take more than 2 sticks!")
        return False
    elif n < 1: # player can take only 1 or 2 sticks 
        print("No you cannot take less than 1 stick!")
        return False
    elif n > sticks: # player can't take 2 when the pile have only 1 stick
        print("There are no enough sticks to take.")
        return False
    else: #player take correctly (follow the rules)
        return True
    
# stick game between computer and human (player2)
while sticks != 0: # loop end when no stick in the pile
    
    #------------------ computer turn (play first) ----------------------
    com_st = random.randint(1, 2)  # computer randomly picks 1 or 2
    print("computer take: ",com_st) # display how many does computer take
    
    # check that human will win or continue the game (didn't end)
    if com_st >= sticks: 
        print('You Win!')
        break # if human will break while loop and print 'You Win!'
    else: # game didn't end 
        sticks -= com_st # update new number sticks in the pile
        print("There are", sticks,"sticks in the pile.") #display the remaining sticks in the pile
    
    #----------------------- player2 (human) turn -----------------------
    # use while loop for keep being asked a number until they take correctly (1 or 2 sticks) 
    while True:
        pla_st = int(input(f"{name},how many sticks you will take (1 or 2):"))
        if player2(pla_st,sticks):
            break # if player2 takes correctly, while loop was break and update new number (remaining) of sticks following line 47
    
    sticks -= pla_st 
    # check that you will lose or continue the game (didn't end)
    if sticks > 0: 
        print("There are", sticks,"sticks in the pile.")
    else:
        print('You Lose!')
        
