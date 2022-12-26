def main():
    time=input("What time is it? ")
    t1=convert(time)
    meals(t1)
def convert(time):
    h,m,=time.split(":")
    h=int(h)
    m=int(m)
    h=h+m/60
    return h
def meals(t1):
    if t1 >=7.00 and t1<=8.00 :
        print("breakfast time")
    elif t1>=12.00 and t1<=13.00 :
        print("lunch time")
    elif t1>=18.00 and t1<=19.00 :
        print("dinner time")
    else:
        print("")
main()