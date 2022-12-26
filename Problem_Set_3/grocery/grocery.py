grocery={}
while True:
    try:
        item=input().lower()
        if item not in grocery:
            grocery[item]=1
        else:
            grocery[item]+=1
    except EOFError:
        for i in sorted(grocery.keys()):
            print(grocery[i],i.upper())
        break
