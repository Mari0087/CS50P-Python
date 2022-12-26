def main():
    test=input('test:').strip()
    result=is_valid(test)
    if result==True:
        print("Valid")
    else:
        print("Invalid")

def is_valid(test):
    length=len(test)
    num=0
    s=test[0:2]
    for i in test:
        if i.isdigit()==True:
            num+=1
    n=list(test[num:])
    count=0
    for i in n:
        if i.isdigit()!=True:
            count+=1
    if num!=0:
        f=n[0]
    else:
        f=n
    l=n[-1]

    if length <= 6 and s.isalpha()==True and f!="0" and len(s)==2 :
        if  num==0:
            return True
        elif count==0 :
            return True
        elif  (f.isdigit()==True or f.isalpha()==True) and l.isdigit()==True:
            return True
        else:
            return False
    else:
        return False

if __name__=="__main__":
    main()