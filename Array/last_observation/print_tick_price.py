from typing import List, Tuple
from datetime import datetime


def print_tick_price(ticks: List[Tuple[float, datetime]], trade_times: List[datetime]) -> List[float]:
    if not ticks:
        raise ValueError('ticks cannot be empty')

    i = 0
    result = []
    price = None
    for trade_time in trade_times:
        while i < len(ticks) and ticks[i][1] <= trade_time:
            price = ticks[i][0]
            i += 1

        result.append(price)

    return result


prices = print_tick_price(ticks=[(50, datetime(2020, 12, 31, 12, 0)),
                                 (51, datetime(2020, 12, 31, 12, 2)),
                                 (52, datetime(2020, 12, 31, 12, 4)),
                                 (53, datetime(2020, 12, 31, 12, 6)),
                                 (54, datetime(2020, 12, 31, 12, 7)),
                                 (55, datetime(2020, 12, 31, 12, 8))],
                          trade_times=[datetime(2020, 12, 31, 12, 1),
                                       datetime(2020, 12, 31, 12, 3),
                                       datetime(2020, 12, 31, 12, 4),
                                       datetime(2020, 12, 31, 12, 5),
                                       datetime(2020, 12, 31, 12, 9)])

assert prices == [50, 51, 52, 52, 55]

prices = print_tick_price(ticks=[(50, datetime(2020, 12, 31, 12, 2)),
                                 (51, datetime(2020, 12, 31, 12, 2)),
                                 (52, datetime(2020, 12, 31, 12, 4)),
                                 (53, datetime(2020, 12, 31, 12, 10))],
                          trade_times=[datetime(2020, 12, 31, 12, 0),
                                       datetime(2020, 12, 31, 12, 1),
                                       datetime(2020, 12, 31, 12, 4),
                                       datetime(2020, 12, 31, 12, 5),
                                       datetime(2020, 12, 31, 12, 7)])

assert prices == [None, None, 52, 52, 52]

