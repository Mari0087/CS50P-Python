
def main():
    greet=input("Greeting:").lower()
    check=greet.strip()
    result=value(check)
    print(result)


def value(check):
    if "h" in check[0]  and "hello" not in check:
        return "$20"
    elif "hello" in check or "hello," in check  :
       return "$0"
    else:
        return "$100"


if __name__ == "__main__":
    main()
