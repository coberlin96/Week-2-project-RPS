import random

def cpu_turn():
    choice = random.randint(1,1000)%3
    move = ''

    if choice == 0:
        move = 'rock'
    elif choice == 1:
        move = 'paper'
    else:
        move = 'scissors'
    return move


def rps():
    player_score = 0
    cpu_score = 0
    name = input("Welcome to rock, paper, scissors! Please enter your name: ")
    while True:
        print(f'{name}: {player_score} \tCPU:{cpu_score}')
        print(f'Enter one of the following: \nRock \nPaper \nScissors \n(or enter quit to exit the program)')
        player_choice = input(f'{name}, make your choice: \n')
        player_choice = player_choice.lower()
        player_choice = player_choice.strip()
        cpu_choice = cpu_turn()
        if cpu_choice == player_choice:
            print("\nIt's a tie!\n")
        elif player_choice == "rock":
            if cpu_choice == "paper":
                print("\nPaper beats rock, you lose.\n")
                cpu_score += 1
            else:  
                print("\nRock beats paper, you win!\n")
                player_score += 1
        elif player_choice == "scissors":
            if cpu_choice == "rock":
                print("\nRock beats paper, you lose\n")
                cpu_score += 1
            else: 
                print("\nScissors beat paper, you win!\n")
                player_score += 1
        elif player_choice == "paper":
            if cpu_choice == "rock":
                print("\nPaper beats rock, you win!\n")
                player_score += 1
            else: 
                print("\nScissors beat paper, you lose\n")
                cpu_score += 1
        elif player_choice == "quit":
            print('Thanks for playing!')
            break
        else:
            print("\nYour input was not one of the valid options, please try again\n") 

rps()