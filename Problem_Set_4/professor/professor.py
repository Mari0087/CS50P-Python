import random

def main():
    level=get_level()
    score=0
    rscore=0
    for i in range(10):
        x,y=generate_integer(level)
        ans=get_ans(x,y)
        check=x+y
        if ans != check :
            rscore=check_ans(x,y,check,rscore)
        score+=1
    score+=rscore
    print(f"Score : {score}")

def get_level():
    while True:
        try:
            level1=int(input("Level:"))
            if 1<=level1<=3:
                return level1
        except:
            pass

def get_ans(x,y):
    try:
        get=int(input(f"{x} + {y} ="))
        return get
    except ValueError :
        pass

def generate_integer(level):
    if level==1:
        x=random.randint(0,9)
        y=random.randint(0,9)
        return x,y
    elif level==2:
        x=random.randint(10,99)
        y=random.randint(10,99)
        return x,y
    elif level==3:
        x=random.randint(100,999)
        y=random.randint(100,999)
        return x,y

def check_ans(x,y,check,rscore):
    count=0
    while count < 2:
        print("EEE")
        get=get_ans(x,y)
        if check == get:
            break
        count +=1
    else:
        print("EEE")
        print(f"{x} + {y} ={check}")
        rscore -=1
    return rscore

if __name__ == "__main__":
    main()