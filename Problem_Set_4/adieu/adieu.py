import inflect

p = inflect.engine()

def main():

    try:
        n=[]
        while True:
            name=input_name()
            n.append(name)
    except EOFError:
        result=p.join(n)
        print(f"Adieu, adieu, to {result}")
def input_name():
    while True:
        name=input("Name:")
        return name



main()