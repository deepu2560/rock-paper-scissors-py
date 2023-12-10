import random

class GameAllFunctions():

  def __init__(self, choice):
    self.player_choice = choice
    self.computer_choice = self.get_computer_choice()

  def get_computer_choice(self):
    choices_dic = {0: "rock", 1: "paper", 2: "scissors"}
    temp = random.randint(0, 2)
    return choices_dic[temp]

  def get_winner(self):
    if self.player_choice == self.computer_choice:
      return f"Match is a tie. You both chose {self.player_choice}"
    elif (self.player_choice == "rock" and self.computer_choice == "paper"
          ) or (self.player_choice == "paper" and self.computer_choice
                == "scissors") or (self.player_choice == "scissors"
                                   and self.computer_choice == "rock"):
      return f"Ohh no, Computer won this time. Computer chose {self.computer_choice}"
    else:
      return f"Hurray, You won the game. Computers choice was {self.computer_choice}"
