"""
Given a stream of stock prices, calculate the average of the latest N prices
"""


def calc_rolling_average(prices: list, window: int):
    if window < 0:
        raise ValueError('window size must be positive')

    if len(prices) < window:
        raise ValueError('number of prices is below the window size')

    rolling_prices = [-1] * window
    last_price_idx = 0
    rolling_sum = sum(prices[:window])
    yield rolling_sum / window

    for p in prices[window:]:
        rolling_sum -= rolling_prices[last_price_idx]
        rolling_sum += p
        last_price_idx = (last_price_idx + 1) % window
        rolling_prices[last_price_idx] = p
        yield rolling_sum / window



try:
    list(calc_rolling_average([1, .6, 9, 3.5], 5))
except ValueError as e:
    print(e)


print(list(calc_rolling_average([4, 2, 6, 7,2, 5, 8, 0, 1, 0], 3)))