import random 

user_win = 0
computer_win = 0

options = ["rock", "paper", "scissors"]

while True:
    user_input = input("Type Rock Paper Scissors or q to quit: ").lower()
    if user_input == "q":
        break
    if user_input not in options:
        continue

    random_number = random.randint(0,2)

    computer_input = options[random_number]
    print("computer picked ", computer_input)

    if user_input == "rock" and computer_input == "scissors":
        print("You won!")
        user_win += 1
    elif user_input == "paper" and computer_input == "rock":
        print("You won! ")
        user_win += 1
    elif user_input == "scissors" and computer_input == "paper":
        print("you won !")
        user_win += 1
   
   
    else:
        print("you lost")
        computer_win += 1

print("you won", user_win, "times")
print("computer won", computer_win, "times")

print("Goodbye")
