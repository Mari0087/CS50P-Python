e=input("Expression:")
x,y,z=e.split()
x=int(x)
z=int(z)
if y == "+":
    print(float(x + z))
elif y == "-":
    print(float(x - z))
elif y == "*":
    print(float(x * z))
elif y == "/":
    print(float(x / z))
else :
    print(float(x % z))