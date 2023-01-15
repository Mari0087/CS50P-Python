fs={
    "F":'Friend',
    "L":'Lover',
    "A":'Affection',
    "M":'Wife',
    "E":'Enemy',
    "S":'Sister',
}

you=input("Enter your name:").replace(' ','').lower()
lover=input("Enter your patner name:").replace(" ","").lower()
name1=list(you)
name2=list(lover)
for i in you:
    for j in lover:
        if i==j:
            try:
                name1.remove(i)
                name2.remove(j)
                break
            except ValueError:
                pass
name=name1+name2
length=len(name)
print(name1,name2,length)
f="FLAMES"
n=1
while n!=len(f):
    trim=length
    while trim>len(f):
        trim=trim-len(f)
    f=f[trim:len(f)]+f[0:trim-1]
print(f"{lover.title()} is your's {fs[f[0]]}")
