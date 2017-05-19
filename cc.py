denominations = [200, 100, 50, 20, 10, 5, 2, 1]

def change(amount, coins = denominations):
    current_coin, *remaining_coins = coins
    if amount == 0:
        return []
    elif amount >= current_coin:
        return change(amount - current_coin, coins) + [current_coin]
    else:
        return change(amount, remaining_coins)
