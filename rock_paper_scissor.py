import random

possible_action = ["rock", "paper", "scissor"]
computer_marks = 0
your_marks = 0

while True:
    computer_action = random.choice(possible_action)
    if(computer_marks == 3 or your_marks == 3):
        if(computer_marks > your_marks):
            print("computer won the game")
            print("Try again")
            break
        else:
            print("congratulation you own the game !!")
            break
    user_action = input("Enter your choice (rock,paper,scissor):")
    print("computer chooses ", computer_action)

    if(user_action == computer_action):
        print("Draw your game ")
        print("Marks does't added")
        print("your marks:", your_marks)
        print("computer marks:", computer_marks)

    elif(user_action == "rock"):
        if(computer_action == "scissor"):
            print("|Rock smashes the scissor ")
            your_marks = your_marks + 1
            print("your marks:", your_marks)
        else:
            print("paper covers the rock")
            computer_marks = computer_marks + 1
            print("computer marks:", computer_marks)

    elif(user_action == "scissor"):
        if(computer_action == "rock"):
            print("Rock smashes the scissor")
            computer_marks = computer_marks + 1
            print("computer marks:", computer_marks)

        else:
            print("scissor cuts the paper ")
            your_marks = your_marks + 1
            print("your marks:", your_marks)

    elif(user_action == "paper"):
        if(computer_action == "rock"):
            print("paper  cover the rock ")
            your_marks = your_marks+1
            print("your marks:", your_marks)

        else:
            print("scissor cuts the paper ")
            computer_marks = computer_marks + 1
            print("computer marks:", computer_marks)
