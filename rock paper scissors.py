import random
player_score=0
computer_score=0
choices=["rock","paper","scissors"]
print("welcome to the game")
print("Type 'exit' to quit the game")
while True:
    player_choice=input("Enter rock,paper, or scissors: ").lower()
    if player_choice=="exit":
        print("Final score - you: {player_score} | computer : {computer_score}")
        print("thanks for applying")
        break
    if player_choice not in choices:
        print("invalid choice! try again")
        continue
    computer_choice=random.choice(choices)
    print(f"computer chose : {computer_choice}")
    if player_choice == computer_choice:
        print("its a tie")
    elif (player_choice == "rock" and computer_choice == "scissors") or (player_choice == "paper" and computer_choice == "rock") or (player_choice == "scissors" and computer_choice == "paper"):
        print("you win")
        player_score+=1
    else:
        print("computer wins")
        computer_score+=1
    print(f"score - you: {player_score} | computer: {computer_score}\n")
    
