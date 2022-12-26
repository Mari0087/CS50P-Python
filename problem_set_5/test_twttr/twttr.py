def main():
    string=input("input: ")
    result=shorten(string)
    print(result,end="")
    print()


def shorten(string):
    print("output:",end="")
    result=""
    for i in string:
        if not i in ['a','e','i','o','u','A','E','I','O','U']:
            result+=i
    return result


if __name__ == "__main__":
    main()