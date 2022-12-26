def main():

        while True:
            s=fuel_m()
            if s>=0 and s<=100:
                if s<=1:
                    print("E")
                elif s>=99:
                    print("F")
                elif s > 0 or s < 100:
                    print(f"{s}%")
                break
            else:
                s=fuel_m()

def fuel_m():
    while True:
        try:
            n = input("Fraction:")
            x,y = n.split("/")
            x=int(x)
            y=int(y)
            s=(x/y)*100
            s=round(s)
            s=int(s)
        except (ZeroDivisionError , ValueError):
            pass
        else:
            return s

main()