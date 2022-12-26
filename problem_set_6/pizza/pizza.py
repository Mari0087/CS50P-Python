from tabulate import tabulate
import sys

def main():
    check_commend_line()
    try:
        with open(sys.argv[1],"r") as lines:
            table=[]
            for line in lines:
                table.append(line.rstrip().split(","))
            head,body=create_table(table)
            print(tabulate(body, headers=head, tablefmt="grid"))
    except FileNotFoundError:
        sys.exit("File does not exist")


def check_commend_line():
    if len(sys.argv)!=2:
        sys.exit("Too many command-line arguments")
    elif ".csv" not in sys.argv[1]:
        sys.exit("Not a csv file")


def create_table(table):
    body=[]
    for i in range(len(table)):
        if i==0:
            head=table[0]
        else:
            body.append(table[i])
    return head,body


if __name__=="__main__":
    main()