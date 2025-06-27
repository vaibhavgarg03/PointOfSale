from Checkout import Checkout

def checkout (item_codes, prices):

    check = Checkout(prices)
    for item in item_codes:
        check.scan(item) 
    return(check.total())

def main():
    print(checkout(['B', 'A', 'A', 'P', 'A','B','B'], {'A': 25, 'B': 40, 'P': 30}))

if __name__ == "__main__":
    main()
    