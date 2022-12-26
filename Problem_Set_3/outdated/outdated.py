month={
    "january": '01',
    "february": '02',
    "march" :'03',
    "april":'04',
    "may":'05',
    "june":'06',
    "july":'07',
    "august":'08',
    "september":'09',
    "october":10,
    "november":11,
    "december":12,
    '1':'01',
    '2': '02',
    '3': '03',
    '4': '04',
    '5':'05',
    '6':'06',
    '7':'07',
    '8':'08',
    '9':'09',
    '10':'10',
    '11':'11',
    '12':'12'
    }
while True:
    try:
        d =input("Date :").lower()
        c=d
        for i in d:
                if  i == "/" or i == "," :
                    d=d.replace(i , " ")
                    break
        m,d,y=d.split()
        p,q,r=c.partition(d)
        p=p.strip()
        r=r.strip()
        if (d.isalpha()==False and m in month) and m==p and r!=y :
            print(f"{y}-{month[m]}-{month[d]}")
            break
        elif m!=p and m.isdigit()==True and r!=y :
            print(f"{y}-{month[m]}-{month[d]}")
            break
    except KeyError:
        pass