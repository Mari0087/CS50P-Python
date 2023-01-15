while True:
    a=int(input("Enter A:"))
    b=int(input("Enter B:"))
    c=int(input("Enter C:"))
    if a!=b and a!=c and b!=c :
        break
    else:
        print("two values same \ninput again:")

if (a<b and b<c) or (a>b and b>c):
    print("2nd large number is",b)
elif (b<a and a<c) or (b>a and a>c):
    print("2nd large number is",a)
elif (a<c and c<b) or (a>c and c>b):
    print("2nd large number is",c)