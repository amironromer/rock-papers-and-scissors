import random
choices = ["rock","paper","scissors"]
computer= random.choice(choices)
player= None
from game import GAME

play=GAME(player,choices,computer)

