# Find biggest difference between two points in array
# Greedy method - update what we've seen so far

stock_prices = [10, 7, 5, 8, 11, 9]


def get_max_profit(stock_prices):

    if len(stock_prices) < 2:
        return IndexError('Profit needs at least 2 prices')

    # Initialize what we know
    min_price = stock_prices[0]
    max_profit = stock_prices[1] - stock_prices[0]

    for index, current_price in enumerate(stock_prices):

        # can't buy and sell at the same time
        if index == 0:
            continue

        # ensure lowest minimum price we've seen so far
        min_price = min(min_price, current_price)

        # what would the current potential profit be
        potential_profit = current_price - min_price

        # compare against maximum profit we've seen so far
        max_profit = max(max_profit, potential_profit)

    return max_profit


print(get_max_profit(stock_prices))
