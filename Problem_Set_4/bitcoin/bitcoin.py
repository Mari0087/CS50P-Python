import sys
import requests
def main():
    while True:
            if len(sys.argv)<2:

                sys.exit("Missing command-line argument")
            elif sys.argv[1].isalpha()==True:
                
                sys.exit("Command-line argument is not a number")
            price=float(get_price())
            price=float(sys.argv[1])*price
            print(f"${price:,.4f}")
            sys.exit()


def get_price():
    value=requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
    json=value.json()
    keys=["bpi","USD","rate_float"]
    for key in keys:
        json=json.get(key)

    return json





if __name__=="__main__":
    main()



