import random

def roll():
    min_value = 1
    max_value = 6
    roll = random.randint(min_value, max_value)
    
    return roll

while True :
    player = input("enter the number of players (1-4): ")
    if player.isdigit():
        player = int(player)
        if 2 <= player <= 4:
            break 
        else:
            print("must be 4")
    else:
        print("invalid, try")

max_score = 50 
player_scors = [0 for _ in range(player)]

print(player_scors)

while max(player_scors) < max_score:
    
    for player_idx in range(player):
        print("\nplayer number", player_idx + 1,"tuen just started!\n" )
        print("your total score is : ", player_scors[player_idx], "\n")
        current_score = 0 
        
        while True:
            should_roll = input("would you like to roll (y)? ")
            if should_roll.lower() != "y" :
                break
            
            
            value =  roll()
            if value == 1:
                print("you rolled a 1! turn done!")
                current_score = 0
                break
            else:
                current_score += value
                print("you rolled a:", value )
                
            print ("your score is :", current_score)
            
    player_scors[player_idx] += current_score
    print("your tota score is :", player_scors[player_idx])
    
max_score = max(player_scors)
winning_idx = player_scors.index(max_score)
print("player number ",winning_idx + 1, "is the winner with a score of: ", max_score )