import random
# 1) we need the random 


# 2) we will also need a function called play
def play():
    # 3) we will also need a variable to stor one of three inputs from the user 
    user = input("What is your choice 'r' for rock, 'p' for paper, 's' for scissor\n")
    # 4) the computer also needs to choose , vatiable to store a random  a list r p s 
    computer = random.choice(['r', 'p', 's'])
    
    # 5) now we need to tell the computer what to do with these choices 
    if user == computer:
        return 'tie'  # 5) if user and computer choose the same its a tie
    
    if is_win(user, computer):
        return 'You won!'
    
    return 'You lost!'
    
def is_win(player, opponent):
    # return true is player wins
    # r > s, s > p, p > r
    if (player == 'r' and opponent == 's') or (player == 's' and opponent == 'p') or (player == 'p' and opponent == 'r'):
        return True
    
print(play())