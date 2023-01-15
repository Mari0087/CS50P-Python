#Big among Three Numbers
a=int(input("a: "))
b=int(input("b: "))
c=int(input("c: "))

#if statement 
#if a>b and a>c :
#    print("A is big")
#elif b>a and b>c :
#    print("b is big")
#elif c>a and c>b :
#    print("c is big")

print("A is big" if (a>b and a>c) else "b is big" if (b>a and b>c) else "c is big" )