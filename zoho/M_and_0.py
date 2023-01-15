import random

n=int(input("n:"))
list1=[]
for i in range(n):
    list2=[]
    rand=("M",0)
    for j in range(n):
        put=random.choices(rand)
        list2.append(put)
    list1.append(list2)

for i in list1:
    for j in i:
        m=i.index(j)
        print(j,":",m,end=" ")
    print()






for i in list1:
    for j in i:
        for k in j:
            print(k,end=" ")
    print()
