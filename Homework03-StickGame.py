sticks = int(input("How many sticks (N) in the pile: ")) # first know all sticks in the pile

print("There are", sticks,"sticks in the pile.") 
name = str(input("What is your name: ")) # ask player name

i = 0 # count pick times start at 0 times
while sticks != 0 : #if sticks in pile equal 0 the loop end
    take = int(input(f"{name},how many sticks you will take (1 or 2):")) # ask player each time that how much do they want to take
    
    # have 4 conditions to check 
    if take > 2: # player can take only 1 or 2 sticks 
        
        print("No you cannot take more than 2 sticks!")
    elif take < 1: # player can take only 1 or 2 sticks 
        
        print("No you cannot take less than 1 stick!")
    elif take > sticks: 
        
        print("There are no enough sticks to take.")
    else:
        i = i + 1 #count when player take correctly
        sticks = sticks - take # sum sticks after player take it
        if sticks > 0:
            print("There are", sticks,"sticks in the pile.")

print("OK. There is no stick left in the pile. You spent", i, "times.")