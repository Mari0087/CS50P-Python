from pyfiglet import Figlet
from random import choice
import sys
figlet=Figlet()

def main():
    if len(sys.argv)==1:
        result = get_input()
        rant=choice(figlet.getFonts())
        figlet.setFont(font = rant)
        print(figlet.renderText(result))
        sys.exit
    elif len(sys.argv)==3:
        if (sys.argv[1]=='-f' or sys.argv[1]=='--font' ) and check()==True :
            result = get_input()
            figlet.setFont(font = sys.argv[2])
            print(figlet.renderText(result))
            sys.exit
        else:
            sys.exit("Invalid usage")
    else:
        sys.exit("Invalid usage")

def get_input():
    text = input("Input:")
    return text

def check():
    for i in figlet.getFonts():
        if sys.argv[2] == i:
            return True

main()