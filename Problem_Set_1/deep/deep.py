x = input("What is the Answer to the Great Question of Life, the Universe, and Everything? ")
x=x.lower().strip()

if x=="42" :
    print("Yes")
elif x=="forty-two" or x=="forty two":
    print("yes")
else:
    print("No")

