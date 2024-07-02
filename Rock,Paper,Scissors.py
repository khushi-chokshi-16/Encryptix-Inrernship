import random
rock= 'ROCK'
paper= 'PAPER'
scissors= 'SCISSORS'
game_actions = [rock, paper, scissors]


while(True):
  user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors and 3 to exit.\n"))
  print(game_actions[user_choice])

  computer_choice = random.randint(0, 2)
  print("Computer chose:")
  print(game_actions[computer_choice])

  if user_choice >= 4 or user_choice < 0: 
    print("You typed an invalid number, you lose!") 
  elif user_choice == 0 and computer_choice == 2:
    print("You win!")
  elif computer_choice == 0 and user_choice == 2:
    print("You lose")
  elif computer_choice > user_choice:
    print("You lose")
  elif user_choice > computer_choice:
    print("You win!")
  elif computer_choice == user_choice:  
    print("It's a draw")
  elif user_choice == 3:
    break




