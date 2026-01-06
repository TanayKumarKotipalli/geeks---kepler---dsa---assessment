"""
Problem: Best Time to Buy and Sell Stock

Approach:
Keep track of the minimum stock price seen so far.
For each day, calculate the profit if sold on that day.
Update the maximum profit accordingly.

Time Complexity: O(n)
Space Complexity: O(1)
"""

def max_profit(prices):
    if not prices:
        return 0

    min_price = prices[0]
    max_profit = 0

    for price in prices[1:]:
        if price < min_price:
            min_price = price
        else:
            max_profit = max(max_profit, price - min_price)

    return max_profit
