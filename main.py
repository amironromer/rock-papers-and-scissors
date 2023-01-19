import random
choices = ["rock","paper","scissors"]
computer= random.choice(choices)
player= None
while player not in choices:
  player=input("rock, paper, and scissors?: ").lower()
  print(computer)
  print(player)
if player==computer:
  print(computer)
  print(player)
  print("TIE!!!!!!!")
elif player=="rock":
  if computer=="paper":
    print(computer)
    print(player)
    print("")




