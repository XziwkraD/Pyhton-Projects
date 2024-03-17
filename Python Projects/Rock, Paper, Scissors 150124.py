import random

def game_result():
    print(f"computer: {computer}")
    print(f"player: {player}")

while True:

    choices = ["rock", "paper", "scissors"]

    computer = random.choice(choices)
    player = None

    while player not in choices: #keeps asking for a proper answer
        player = input("rock, paper, or scissors?: ").lower()

    if player == computer:
        game_result()            
        print("Its a tie!")
    
    elif player == "rock":
        if computer == "paper":
            game_result()
            print("You lose!")
        if computer == "scissors":
            game_result()
            print("You win!")

    elif player == "paper":
        if computer == "scissors":
            game_result()
            print("You lose!")
        if computer == "rock":
            game_result()
            print("You win!")

    elif player == "scissors":
        if computer == "rock":
            game_result()
            print("You lose!")
        if computer == "paper":
            game_result()
            print("You win!")

    play_again = input("Play again? (yes/no): ").lower()

    if play_again != "yes":
        print("Thanks for playing!")
        break