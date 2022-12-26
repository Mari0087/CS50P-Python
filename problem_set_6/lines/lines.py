import sys

def main():
    check_commend_line()
    count=0
    try:
        with open(sys.argv[1],"r") as lines:
            for line in lines:
                if code_line_count(line):
                    count+=1
    except FileNotFoundError:
        sys.exit("File does not exist")

    print(count)


def check_commend_line():
    if len(sys.argv)!=2:
        sys.exit("Too many command-line arguments")
    elif ".py" not in sys.argv[1]:
        sys.exit("Not a Python file")

def code_line_count(line):
    if line.isspace():
        return False
    if line.lstrip().startswith("#"):
        return False
    return True


if __name__=="__main__":
    main()