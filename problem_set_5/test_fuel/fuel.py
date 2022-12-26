def main():
    while True:
        try:
            n = input("Fraction:")
            s=convert(n)
        except (ZeroDivisionError , ValueError):
            pass
        else:
            if s<=100 :
                result=gauge(s)
                print(result)
                break

def convert(n):
    x,y = n.split("/")
    x=int(x)
    y=int(y)
    s=(x/y)*100
    s=round(s)
    s=int(s)
    return s


def gauge(s):
    if s>=0 and s<=100:
        if s<=1:
            return "E"
        elif s >=99 :
            return "F"
        elif s > 0 or s < 100:
            return f"{s}%"
if __name__=="__main__":
    main()