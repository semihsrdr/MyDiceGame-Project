#MyDiceGame Beginner Level Project

import random
import time

print("Welcome to the 'Dice Game'...")
print("In this game you will compete against computer")
print("Game will created for best of three. That means someone will win who reached the 2 points first.")
while True:
    yes=input("Do you wanna start (yes,no) : ")

    computer_point=0
    player_point=0

    if yes.lower()=="yes":

        while computer_point < 2 and player_point < 2:
            print("-------------------------------------------------------------------------------")
            print("Dices are throwing...")
            time.sleep(2)
            player_dice=random.randint(1,6)
            computer_dice=random.randint(1,6)
            print("Player Dice is :",player_dice)
            print("Computer Dice is : ",computer_dice)

            if player_dice > computer_dice:
                player_point+=1
                print("Player Wins the turn")
            elif player_dice < computer_dice:
                computer_point+=1
                print("Computer Wins the turn")
            else:
                print("The Dices are equals!")

        print("----------------------------------------------------------------------------------------------")

        print("Result : ")
        if player_point==2:
            print("Player Won",player_point,"-",computer_point)
        else:
            print("Computer Won",computer_point,"-",player_point)


        print("----------------------------------------------------------------------------------------------")

    elif yes.lower()=="no":
        print("The game is shutting down...")
        time.sleep(1)
        print("The game Shutted Down")
        break