from Checkout import Checkout

def checkout (item_codes, prices):

    check = Checkout(prices)
    for item in item_codes:
        check.scan(item)
    return(check.total())