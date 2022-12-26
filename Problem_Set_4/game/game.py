import random
import sys

def main():
        level=get_input()
        rand=random.randint(1,level)
        while True:
                guess=get_guess(level)
                if guess < rand:
                    print("Too small!")
                elif guess > rand :
                    print("Too large!")
                elif guess == rand:
                    print("Just right!")
                    sys.exit()
def get_input():
    while True:
        try:
            level=int(input("level:"))
            if 1<=level:
                return level
        except ValueError:
            pass
def get_guess(level):
    while True:
        try:
            guess=int(input("guess:"))
            if 1 <= level:
                return guess
        except ValueError:
            pass


main()