import random

user_score = 0
computer_score = 0
game_options = ["rock", "paper", "scissors"]
while True:
    user_choice = input("Enter Rock/Paper/Scissors:").lower()  # taking user input

    if user_choice in game_options:
        random_number = random.randint(0, 2)  # to choose randomly in game_options
        computer_pick = game_options[random_number]
        print(f"You picked: {user_choice}")
        print(f"Computer picked: {computer_pick}")
        if user_choice == "rock" and computer_pick == 'scissors':
            print("YOU WIN!!")
            user_score += 1
        elif user_choice == "paper" and computer_pick == 'rock':
            print("YOU WIN!!")
            user_score += 1
        elif user_choice == "scissors" and computer_pick == 'paper':
            print("YOU WIN!!")
            user_score += 1
        elif user_choice == computer_pick:
            print("YOU BOTH PICKED SAME.CONTINUE!!")
        else:
            print("COMPUTER WINS!!")
            computer_score += 1

        choice = input("Do you want to quit?(yes/no)")
        if choice == "yes":
            break

    else:
        print("Invalid option")
