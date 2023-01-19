def GAME(player,choices,computer):
  while True:
    
    while player not in choices:
      player=input("rock, paper, and scissors?: ").lower()
      print(computer)
      print(player)
    if player==computer:
      print(computer)
      print(player)
      print("TIE!!!!!")
    elif player=="rock":
      if computer=="paper":
        print(computer)
        print(player)
        print("You lose!!!!!")  
      if computer=="scissors":
        print(computer)
        print(player)
        print("You win!!!!!")
    elif player=="scissors":
      if computer=="rock":
        print(computer)
        print(player)
        print("You lose!!!!!")  
      if computer=="paper":
        print(computer)
        print(player)
        print("You win!!!!!")
    elif player=="paper":
      if computer=="scissors":
        print(computer)
        print(player)
        print("You lose!!!!!")  
      if computer=="rock":
        print(computer)
        print(player)
        print("You win!!!!!")
    play_again=input("Play again? (yes/no): ").lower()
    if play_again != "yes":
      break
  print("bye")