import random


# 1) List of choices
choices = ["rock", "paper","scissors"] 

# 2) Computer generates random choice
computer = random.choice(choices)      

# 3) Player input's choice
player = input("Pick: rock, paper or scissors : " )  

print("computer: ", computer)          # Computer's choice
print("player: ", player)              # Player's choice