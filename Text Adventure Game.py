#Python Text Adventure Game

import time
import random
inventory1 = ["torch", "pencil", "elastic band", "catapult", "rope", "parcel"]
difficulty = "unknown"
luck = ["1", "2", "3", "4"]

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

#-------------------------
#I only activate this line for testing hp += 1000
inventory1 = ["torch", "torch"]
#-------------------------

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
        time.sleep(3)
        print("You lose 10 health points.")
        hp -= 10
        print("You now have ", hp, " health points.")
        time.sleep(2)
        if hp <= 0:
            print("You are dead. I am sorry for your loss.")
            print("GAME OVER")
            break
        print("The snake bite hurts but isn't fatal.")
        time.sleep(2)
        print("You decide that you will need a weapon to defend yourself with.")
        time.sleep(3)
        print("You search in your bag for a weapon.")
        item1 = random.choice(inventory1)
        print("You find '", item1, "'.")
        time.sleep(3.5)
        if item1 == "torch":
            print("As you have a torch, you decide to investigate the cave systems.")
            time.sleep(1.5)
            print("You stumble upon a fast flowing river with a rickety bridge over it.")
            time.sleep(3)
            print("You realise that you must cross the bridge to continue.")
            time.sleep(2)
            print("Do you cross the bridge:")
            print("a: quickly?")
            print("b: slowly and carefully?")
            haste1 = input("a or b?")
            haste1 = haste1.lower()
            if haste1 == "a":
                print("You begin to sprint accross the bridge.")
                time.sleep(2)
                print("When you are half way accross you step on a plank and it breaks.")
                time.sleep(3)
                print("You fall into the fast flowing river and...")
                time.sleep(3)
                print("You are soon swept underwater by the strong currents and...")
                time.sleep(3)
                print("You lose conciousness...")
                time.sleep(5)
                print("And 30 health points.")
                time.sleep(1)
                hp -= 30
                print("You now have ", hp, " health points.")
                time.sleep(2)
                if hp <= 0:
                    print("You are dead. I will miss you.")
                    print("GAME OVER")
                    break
                print("When you wake you find yourself on a raised plinth in the middle of what looks like a maze.")
                time.sleep(3)
                print("Do you:")
                time.sleep(1)
                print("a: Look in your bag for some string to help you navigate the maze?")
                print("b: Jump down into the maze and head vaguely for the direction of the centre?")
                print("c: Give up, stay where you are and hope that help comes before you starve?")
                time.sleep(1)
                answer1 = input("a, b or c?")
                answer1 = answer1.lower()
                if answer1 == "a":
                    print("You look in you bag for some string.")
                    luckiness = random.choice(luck)
                    if luckiness == "1" or "2":
                        print("You found string!")
                        time.sleep(2)
                        print("You lay down string as you navigate the complex maze")
                        time.sleep(1)
                        print("You get lost a few times but successfully use the string to find the way back...")
                        time.sleep(3)
                        print("You eventually get out of the maze.")
                if answer1 == "d":
                    print("You are so groovy that you win automatically!")
                    print("Congratulations!")
                    break
                print("TBC (this section hasn't been made yet)")
                break
            if haste1 == "b":
                print("You cross the bridge slowly and carefully...")
                time.sleep(2)
                print("You step on a plank which breaks beneath you...")
                time.sleep(2)
                print("Luckily, as you are going slowly, you recover your balance and...")
                time.sleep(3)
                print("You make it safely to the other side.")
                print("TBC (this section hasn't been made yet)")
                break
                
    if direction1 == "right":
        print("TBC (this section hasn't been made yet)")

