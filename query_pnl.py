from typing import List
from collections import defaultdict


def get_net_profit(events: List[str]) -> List[int]:
    portfolio = defaultdict(int)
    price_changes = defaultdict(int)
    total_pnl = 0
    ans = []

    for event in events:
        parts = event.split()
        event_type = parts[0]

        if event_type == 'BUY' or event_type == 'SELL':
            product = parts[1]
            quantity = int(parts[2])
            if event_type == 'BUY':
                portfolio[product] += quantity
            else:
                portfolio[product] -= quantity
                total_pnl += price_changes[product] * quantity
        elif event_type == 'CHANGE':
            product = parts[1]
            price_change = float(parts[2])
            price_changes[product] += price_change

        elif event_type == 'QUERY':
            for p, qty in portfolio.items():
                total_pnl += price_changes[p] * qty

            ans.append(total_pnl)

        return ans


events = [
    'BUY'
    ]
print()


