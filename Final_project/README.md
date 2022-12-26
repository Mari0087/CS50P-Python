Snake and ladder is a simple game consists of snakes and ladders. The object of the game is to navigate one's game piece, according to die rolls, from the start (bottom square) to the finish (top square), helped or hindered by ladders and snakes respectively.

This is a python based version of this game.

Libraries Used:-

Random Module is a built-in module to generate the pseudo-random variables. It can be used perform some action randomly such as to get a random number, selecting a random elements from a list, shuffle elements randomly, etc. And sys Module is using exit to the program

Let's start :




Dictionary of ladder and snake such that ladder={start_point:ending_point},snake={ending_point,starting_point} ladder = {1: 38, 4: 14, 8: 30, 21: 42, 28: 76, 50: 67, 71: 92, 80: 99}, snake = {32: 10, 36: 6, 48: 26, 62: 18, 88: 24, 95: 56, 97: 78}


project Functions:


def main(): This Function is asked for count of players ,asked for player name and checks weather a points has reached end point that is 100.

def roll_dice():This Function is needed to dice is roll randomly between (1,6).

def turn(name,i,press,p): This Function needed to check player continue the game? or Stop?.

def move(dice,i,name,p): This function used to picese moving points calculation.



test_project Functions:


def test_roll_dice(): Test on roll_dice() function generate number randomly between (1,6).

def test_turn(name,i,press,p): Test on turn(name,i,press,p) function check player continue the game? or Stop?.

def test_move(dice,i,name,p): Test on move(dice,i,name,p) function picese moving points calculation.