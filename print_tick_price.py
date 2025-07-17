from typing import List, Tuple
from datetime import datetime


def print_tick_price(ticks: List[Tuple[float, datetime]], trade_times: List[datetime]) -> List[float]:
    if not ticks:
        raise ValueError('ticks cannot be empty')

    i = 0
    result = []
    for trade_time in trade_times:

        tick_price, tick_time = ticks[i]
        if tick_time == trade_time:
            result.append(tick_price)

        elif tick_time < trade_time:
            while tick_time <= trade_time and i < len(ticks) - 1:
                i += 1
                tick_price, tick_time = ticks[i]

            i = (i - 1) if tick_time > trade_time else i
            result.append(ticks[i][0])

        else:
            result.append(None)


    # i, j = 0, 0
    # result = []
    # while j < len(trade_times):
    #     trade_time = trade_times[j]
    #     tick_price, tick_time = ticks[i]
    #     while i < len(ticks) - 1 and tick_time < trade_time:
    #         i += 1
    #         tick_price, tick_time = ticks[i]
    #
    #     i = i if tick_time == trade_time else (i - 1)
    #     result.append(ticks[i][0])
    #
    #     j += 1

    return result



prices = print_tick_price([(50, datetime(2020, 12, 31, 12, 0)),
                  (51, datetime(2020, 12, 31, 12, 2)),
                  (52, datetime(2020, 12, 31, 12, 4))],
                 [datetime(2020, 12, 31, 12, 1),
                  datetime(2020, 12, 31, 12, 3),
                  datetime(2020, 12, 31, 12, 4),
                  datetime(2020, 12, 31, 12, 5)])

print(prices)


prices = print_tick_price([(50, datetime(2020, 12, 31, 12, 2)),
                  (51, datetime(2020, 12, 31, 12, 2)),
                  (52, datetime(2020, 12, 31, 12, 4)),
                  (53, datetime(2020, 12, 31, 12, 10))],
                 [datetime(2020, 12, 31, 12, 0),
                  datetime(2020, 12, 31, 12, 1),
                  datetime(2020, 12, 31, 12, 4),
                  datetime(2020, 12, 31, 12, 5),
                  datetime(2020, 12, 31, 12, 7)])

print(prices)
