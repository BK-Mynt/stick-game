# Stick Game Ver3
# improve computer
# has x sticks
# make computer win 
# computer start first

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
#----------------------------- list num of sticks that make com win ----------------------------    
# list of num sticks in the pile that computer has to make for player turn and it will garuntee that computer always win
# pattern is 1, 4, 7, 10, 13, 16, 19, 22,... 

def check_st(sticks):
    i = 0
    num_check = []

    while True:
        y = 3 * i + 1
        if y > sticks:
            break
        num_check.append(y)
        i += 1
    return num_check
    
# list of num_check will return list of pattern that make com win the game if com can make it for player turn
    
#------------------------------ game play between com and human --------------------------------    
# loop end when no stick in the pile
while sticks != 0: 
    
    win_con = check_st(sticks) #
    #------------------ computer turn (play first) ----------------------
    # win condition for com picking the sticks from the pile 
    if sticks > win_con[-1]:
        if sticks - win_con[-1] == 1:
            com_st = 1
        elif sticks - win_con[-1] == 2:
            com_st = 2
    else:
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

#---------------------------------- remark -------------------------------        
# if player knows the strategy of this game and chose 4, 7, 10,... sticks in the pile at the begining
# computer which the first player can't win 
# if player don't know the strategy and chose 4, 7, 10,... sticks in the pile at the begining
# computer can win the game       