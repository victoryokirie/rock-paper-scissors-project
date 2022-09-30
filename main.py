rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇


print("Welcome to the Rock, Paper, Scissors game!")
player_choice=int(input("What do you choose? Type 0 for Rock, 1 for Paper and 2 for Scissors...\n"))

Game_options=[rock, paper, scissors]






if player_choice >= 3 or player_choice < 0:
    print("please enter a valid number... You lose!")
else: 
    print(Game_options[player_choice])
    ##Computer choice
    import random
    computer_choice=random.randint(0,2)
    print("computer chose:")
    print(Game_options[computer_choice])

    if player_choice == 0 and computer_choice == 2:
        print("you win!")
    elif player_choice == computer_choice:
        print("It's a draw!")
    elif computer_choice == 0 and player_choice == 2:
        print("You lose!")
    elif computer_choice > player_choice:
        print("you lose!")
    elif player_choice > computer_choice:
        print("You win!")

