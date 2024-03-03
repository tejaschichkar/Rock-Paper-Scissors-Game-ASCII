"""

On first line in input enter y or n to know that you want to play or not
on the second line enter Rock, Paper or Scissors. the first letter of this words should be capital

"""

import random as rndm

R = """ 
      _______
    ---'   ____)
          (_____)
          (_____)
          (____)
    ---.__(___)

        """
P = """
        _______
    ---'   ____)____
              ______)
              _______)
             _______)
    ---.__________)

        """
S = """
        _______
    ---'   ____)____
              ______)
           __________)
          (____)
    ---.__(___)
        """
def game():
    player = input("enter Rock, Paper or Scissors\n") or rndm.choice(['Rock','Paper','Scissors']) 
    if player == "Rock":
        print("Player chose\n", R)
    elif player == "Paper":
        print("Player chose\n", P)
    elif player == "Scissors":
        print("Player chose\n", S)
    
    computer = rndm.choice(['Rock', 'Paper', 'Scissors'])
    if computer == "Rock":
        print("computer chose\n", R)
    elif computer == "Paper":
        print("computer chose\n", P)
    elif computer == "Scissors":
        print("computer chose", S)
    
    print("-"*39+"|")
    print("players choice is " + player)
    print("-"*29+"|")
    print("computers choice is " + computer)
    print("-"*29+"|")
    
    if player == computer:
       print("TIE")
       print("Congrats to both !")
    elif player == "Rock":
        if computer == "Paper":
           print("YOU LOSE")
           print("Better luck next time !")
        else:
            print("YOU WON")
            print("Congratulations for victory !")
    
    elif  player == "Paper":
        if computer == "Scissors":
           print("YOU LOSE")
           print("Better luck next time !")
        else:
            print("YOU WON")
            print("Congratulations for victory !")
    
    elif  player == "Scissors":
        if computer == "Rock":
           print("YOU LOSE")
           print("Better luck next time !")
        else:
            print("YOU WON")
            print("Congratulations for victory !")
    print("-"*39+"|")

"""
if you're using any python ide then
use while loop instead of if loop
"""
play = input("Do you want to play ? y/n\n")
if play == "y":
    game()
elif play == "n":
    print("Thanks for visiting ❤❤❤")