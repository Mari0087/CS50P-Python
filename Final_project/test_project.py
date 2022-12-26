import project


def test_turn():#test_turn(name,i,press,p)

    # Press Enter dice is roll
    assert project.turn(["MARI","SELVA"],1,"",[65,87,0,0])=="\n          SELVA last score is 87"
    assert project.turn(["MARI","SELVA"],0,"",[65,87,0,0])=="\n          MARI last score is 65"

    # Enter stop then program exit
    try:
        assert project.turn(["MARI","SELVA"],1,"stop",[65,87,0,0])==SystemExit
    except SystemExit:
        pass


def test_roll_dice():#test_roll_dice()

    # Roll the dice
    assert project.roll_dice()<=6 and project.roll_dice()>=1



def test_move():#test_move(dice,i,name,p)
    # piece moving point
    assert project.move(5,0,["MARI","SELVA"],[65,87,0,0])==70
    assert project.move(1,1,["MARI","SELVA"],[65,99,0,0])==100
    assert project.move(5,0,["MARI","SELVA"],[95,87,0,0])==100

    #piece lands on the head of a snake
    assert project.move(5,0,["MARI","SELVA"],[90,87,0,0])==56

    #piece lands at the bottom of a ladder
    assert project.move(1,1,["MARI","SELVA"],[65,20,0,0])==42

    #piece is out of range than
    assert project.move(5,1,["MARI","SELVA"],[65,97,0,0])==97