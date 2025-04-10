import random

def roll():
    min_value = 1
    max_value = 6
    roll = random.randint(min_value, max_value)
    
    return roll

value = roll()
print(value)

while True:
    players = input("Enter the number of players (2 - 4): ")
    if players.isdigit():
            players = int(players)
            if 2 <= players <= 4:
                break
            
            else:
                 print("Invalid, try again")
print(players)

max_score = 50
player_scores = [0 for _ in range(players)]


while max(player_scores) < max_score:
     
    for players_idx in range(players):
        print("\nPlayer", players_idx + 1, "Turn has just started! \n")
        print("your total score is:", player_scores[players_idx], "\n")
        current_score = 0
   
   
        while True:
            should_roll = input("Wouild you like to roll (y)? ")
            
            
            if should_roll.lower() != "y":
                print("Turn skipped.")  
                break  
    
            value = roll()
            
            
            if value == 1: 
                print("You rolled a 1! Turn done!")
                current_score = 0
                break
    
            else:
                current_score += value
                print(":you rolled a:", value)
                print("Your score is:", current_score)


        player_scores[players_idx] += current_score
        print("Your total score is:", player_scores[players_idx])

max_score = max(player_scores)
winning_idx = player_scores.index(max_score)
print("Player number", winning_idx + 1,"is the winner with the score of:", max_score)
