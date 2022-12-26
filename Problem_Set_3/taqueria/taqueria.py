def main():
    s={
        "baja taco": 4.00,
        "burrito": 7.50,
        "bowl": 8.50,
        "nachos": 11.00,
        "quesadilla": 8.50,
        "super burrito": 8.50,
        "super quesadilla": 9.50,
        "taco": 3.00,
        "tortilla salad": 8.00
    }
    try:
        input_m(s)
    except EOFError:
        pass
def input_m(s):
    v=0
    while True:
        item=input("Item:").lower()
        if item in s:
            v=v+s[item]
            print(f"Totel:${v}0")
        elif item != "":
            item=input("Item:").lower()
        else:
            break
main()