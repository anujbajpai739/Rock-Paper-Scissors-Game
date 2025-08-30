# This is random library which allows to make random selections with things it is called
import random

# This function is used to take user choice as input and then set it in the list element with randomized computer choice 

def get_choice():
  player_choice = input("Enter a choice (rock, paper, scissors): ")

# This is a LIST which can store different elements
  options = ["rock", "paper", "scissors"]

  computer_choice = random.choice(options)

  choices = {"player": player_choice, "computer" : computer_choice}

  return choices    # Function definition ends here!!

# This function checks who won

def check_win(player, computer):


  # print what player and computer chose
  print(f"You chose: {player}, computer chose: {computer} ;>")


  # if they chose same 
  if player == computer:
    return "It's a tie!!"
  

  # if player chose rock then 
  elif player == "rock":

    if computer == "paper":
      return "OOPS!! Computer wins this time!!"
    else:
      return "Hurray!! You <<<<<WON>>>>> -----> <: * :>"
    

  # if player chose paper then  
  elif player == "paper":

    if computer == "scissors":
      return "OOPS!! Computer wins this time!!"
    else:
      return "Hurray!! You <<<<<WON>>>>> -----> <: * :>"
    

  # if player chose scissors then  
  elif player == "scissors":

    if computer == "paper":
      return "OOPS!! Computer wins this time!!"
    else:
      return "Hurray!! You <<<<<WON>>>>> -----> <: * :>"   # Function definition ends here!!
    


# getting our both choices as list declared in function retrieved in choices variable
choices = get_choice()

# taking result using check win function
result = check_win(choices["player"], choices["computer"])

print(result)