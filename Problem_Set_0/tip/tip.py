def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")

def dollars_to_float(d):
    d1 =d.replace("$","")
    return float(d1)

def percent_to_float(p):
    d1=p.replace("%","")
    d2=float(d1)/100
    return float(d2)

main()