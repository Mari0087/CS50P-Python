d =input()
for i in d:
    if  i == ";" :
        d=d.replace(i , " ")
m=d.split()
sum=0
for j in m:
    sum+=int(j)
print(sum)