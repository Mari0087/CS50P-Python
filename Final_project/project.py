                    #snake and ladder
#rules
"""1.Minimum Two player, Maximum Four players played.
2.roll the dice. Move your piece forward the number of spaces shown on the dice.
3.If your piece lands at the bottom of a ladder, you can move up to the top of the ladder.
4.If your piece lands on the head of a snake, you must slide down to the bottom of the snake.
5.The frist player to reach 100 that player is the winner."""

import random
import sys

def main():
    # Number of Players (2 to 4)
    while True:
        count=int(input("How many players are in the game? "))
        # count of players
        if count>1 and count<=4:
            break
        else :
            print("Wrong input\nplease, enter between 2 to 4")

    # Name of the players
    # list declare or empty list
    name=["","","",""]
    # get players name
    for i in range(count):
        name[i] = input(f"What is the name of Player {i+1} ? ").upper()

    print("\n",name[0], name[1], name[2], name[3], "- Welcome To Snakes And Ladders\n")

    # pieces starting point
    p=[0,0,0,0]
    while True:
        for i in range(count):
            # players Turn
            # get Enter or stop
            press=input(f"{name[i]} Press Enter to continue or Enter 'stop' to stop ")
            print(turn(name,i,press,p))

            # Roll the dice
            dice=roll_dice()
            print(f"          {name[i]} Rolled a {dice}")

            #piece moves
            p[i]=move(dice,i,name,p)

            print(f"          {name[i]}, your current square is {p[i]}\n")
            # if p[i] if 100 than game over winner
            if p[i]==100:
               sys.exit(f"\n\nCONGRATULATIONS {name[i]},YOU WIN THE GAME!\n\n")

def turn(name,i,press,p):
    # Enter stop then program exit
    if press.lower()=="stop":
        return sys.exit("\n\nGame Over\n\n")
    # Press Enter dice is roll
    else:
        return f"\n          {name[i]} your last square is {p[i]}"

def roll_dice():
    # Roll the dice
    dice=random.randint(1,6)
    return dice

def move(dice,i,name,p):
    # piece moving point
    p[i]+=dice
    # snake and ladder point
    snake = {32: 10, 36: 6, 48: 26, 62: 18, 88: 24, 95: 56, 97: 78}
    ladder = {1: 38, 4: 14, 8: 30, 21: 42, 28: 76, 50: 67, 71: 92, 80: 99}
    # if p[i] in snake then down
    if p[i] in snake :
        snake_head=p[i]
        print(f"{name[i]} : your piece land a snake ")
        p[i]=snake[p[i]]
        # Snake starting point to ending point
        print(f"piece move on {snake_head} to {p[i]}")
    #if p[i] in ladder then up
    if p[i] in ladder:
        ladder_bottom=p[i]
        print(f"{name[i]} : your piece land a ladder ")
        p[i]=ladder[p[i]]
        # ladder starting point to ending point
        print(f"piece move on {ladder_bottom} to {p[i]}")
    # if p[i] is out of range than
    if p[i] > 100:
        p[i]-=dice
        print(f"{name[i]}: BAD LUCK, YOU CANT MOVE, YOU NEED A {100-p[i]} TO WIN")
    return p[i]

if __name__=="__main__":
    main()