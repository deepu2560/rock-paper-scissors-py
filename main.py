from game_functions import GameAllFunctions

def Play_the_game():
  print("Let's play Rock, Paper, Scissors")
  user_choice = input("Enter your choice: \n")
  game = GameAllFunctions(user_choice.lower())
  print(game.get_winner())


game_is_running = True

while (game_is_running):
  Play_the_game()
  playing_choice = input("Want to play again? N for no: \n")
  if playing_choice.lower() == "n":
    game_is_running = False
