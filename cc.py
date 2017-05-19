denominations = [200, 100, 50, 20, 10, 5, 2, 1]

def change(amount):
    coins = []
    for coin in denominations:
        while amount >= coin:
            coins.append(coin)
            amount -= coin
    return coins[::-1]
