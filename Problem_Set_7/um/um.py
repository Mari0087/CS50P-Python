import re

def main():
    text=input("Text: ")
    result=count(text)
    print(result)

def count(s):
    return len(re.findall(r"^um\b|(?<=\s)um\b", s, re.IGNORECASE))


if __name__ == "__main__":
    main()