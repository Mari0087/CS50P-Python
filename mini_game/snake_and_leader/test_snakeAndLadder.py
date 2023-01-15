import snakeAndLadder


def test_turn():#test_turn(name,i,press,p)

    # Press Enter dice is roll
    assert snakeAndLadder.turn(["MARI","SELVA"],1,"",[65,87,0,0])=="\n          SELVA last score is 87"
    assert snakeAndLadder.turn(["MARI","SELVA"],0,"",[65,87,0,0])=="\n          MARI last score is 65"

    # Enter stop then program exit
    try:
        assert snakeAndLadder.turn(["MARI","SELVA"],1,"stop",[65,87,0,0])==SystemExit
    except SystemExit:
        pass


def test_roll_dice():#test_roll_dice()

    # Roll the dice
    assert snakeAndLadder.roll_dice()<=6 and snakeAndLadder.roll_dice()>=1



def test_move():#test_move(dice,i,name,p)
    # piece moving point
    assert snakeAndLadder.move(5,0,["MARI","SELVA"],[65,87,0,0])==70
    assert snakeAndLadder.move(1,1,["MARI","SELVA"],[65,99,0,0])==100
    assert snakeAndLadder.move(5,0,["MARI","SELVA"],[95,87,0,0])==100

    #piece lands on the head of a snake
    assert snakeAndLadder.move(5,0,["MARI","SELVA"],[90,87,0,0])==56

    #piece lands at the bottom of a ladder
    assert snakeAndLadder.move(1,1,["MARI","SELVA"],[65,20,0,0])==42

    #piece is out of range than
    assert snakeAndLadder.move(5,1,["MARI","SELVA"],[65,97,0,0])==97