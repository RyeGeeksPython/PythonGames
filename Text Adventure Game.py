#Python Text Adventure Game

import time
import random
inventory1 = ["torch", "pencil", "elastic band", "catapult", "rope", "parcel"]
difficulty = "unknown"

print("In this game you lose or gain health points depending on the decisons you make.")
time.sleep(2)
while difficulty != "easy" or "normal" or "hard" or "expert":
    print("What difficulty setting would you like to play on:")
    difficulty = input("Easy, normal, hard or expert?")
    difficulty = difficulty.lower()

    if difficulty == "easy":
        hp = 80
        break
    if difficulty == "normal":
        hp = 50
        break
    if difficulty == "hard":
        hp = 30
        break
    if difficulty == "expert":
        hp = 1
        break

print("You currently have ", hp, " health points.")
time.sleep(3)
print("START")
print("You are standing on a path at the end of a jungle. There is a cave to your left and a beach to your right.")
time.sleep(2.5)

#Loop until I get a recognised response
while True:
    direction1 = input("Do you want to go left or right?")
    #Convert to lower case to accept variations
    direction1 = direction1.lower()
    #if they decide to go LEFT
    if direction1 == "left":
        print("You walk to the cave and notice there is an opening.")
        time.sleep(1)
        print("As you aproach the opening you are bitten by a small snake.")
        time.sleep(2)
        print("You lose 20 health points.")
        hp -= 20
        print("You now have ", hp, " health points.")
        time.sleep(2)
        if hp <= 0:
            print("You are dead. I am sorry for your loss.")
            break
        print("The snake bite hurts but isn't fatal.")
        time.sleep(2)
        print("You decide that you will need a weapon to defend yourslef with.")
        time.sleep(2.5)
        print("You search in your bag for a weapon.")
        item1 = random.choice(inventory1)
        print("You find '", item1, "'.")
        time.sleep(3)
        if item1 == "torch":
            print



