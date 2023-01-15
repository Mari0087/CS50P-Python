import random

num=int(input("n:"))
list1=[]
list3=[]
for i in range(num):
    list2=[]
    for j in range(num):
        count=0
        while True:
            value=0
            value=random.randint(32,124)
            value=chr(value)
            list3.append(value)
            for i in list3:
                if i==value:
                    count+=1
            if count<=2:
                list2.append(value)
                break          
    list1.append(list2)
for i in list1:
    for j in i:
        print(j,end=" ")
    print()