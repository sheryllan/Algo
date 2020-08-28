"""
Say you have an array for which the i-th element is the price of a given stock on day i.

Design an algorithm to find the maximum profit. You may complete at most k transactions.

Note:
You may not engage in multiple transactions at the same time (ie, you must sell the stock before you buy again).

Example 1:

Input: [2,4,1], k = 2
Output: 2
Explanation: Buy on day 1 (price = 2) and sell on day 2 (price = 4), profit = 4-2 = 2.
Example 2:

Input: [3,2,6,5,0,3], k = 2
Output: 7
Explanation: Buy on day 2 (price = 2) and sell on day 3 (price = 6), profit = 6-2 = 4.
             Then buy on day 5 (price = 0) and sell on day 6 (price = 3), profit = 3-0 = 3.
"""

class Solution:
    def heapify(self, A, i, n):
        smallest = i
        left = 2 * i + 1
        right = 2 * i + 2

        if left < n and A[left] < A[smallest]:
            smallest = left
        if right < n and A[right] < A[smallest]:
            smallest = right

        if smallest != i:
            A[i], A[smallest] = A[smallest], A[i]
            self.heapify(A, smallest, n)


    # 2D dp solution with complexity k * n ^ 2
    def maxProfit(self,  k: int, prices: [int]):
        if not prices:
            return 0
        buy_sell_prices = []
        last_price, buy_price = prices[0], prices[0]
        for p in prices[1:]:
            if p < last_price:
                if last_price > buy_price:
                    buy_sell_prices.append(buy_price)
                    buy_sell_prices.append(last_price)
                buy_price = p
            last_price = p

        if last_price > buy_price:
            buy_sell_prices.append(buy_price)
            buy_sell_prices.append(last_price)

        if not buy_sell_prices:
            return 0

        N = len(buy_sell_prices) // 2
        if N <= k:
            return sum(buy_sell_prices[2 * x + 1] - buy_sell_prices[2 * x] for x in range(N))

        dp = [{} for _ in range(N)]
        dp[-1][1] = buy_sell_prices[-1] - buy_sell_prices[-2]

        def calc_profit(i_buy, n):
            n = min(n, N - i_buy)
            if n <= 0:
                return 0
            if n in dp[i_buy]:
                return dp[i_buy][n]

            max_profit = calc_profit(i_buy + 1, n)
            buy_price = buy_sell_prices[2 * i_buy]
            for i in range(i_buy, min(N, i_buy + N - k + 1)):
                sell_price = buy_sell_prices[2 * i + 1]
                if sell_price < buy_price:
                    continue
                profit = sell_price - buy_price + calc_profit(i + 1, n - 1)
                max_profit = max(max_profit, profit)

            dp[i_buy][n] = max_profit
            return max_profit

        return calc_profit(0, k)


s = Solution()
assert s.maxProfit(4, [1,2,4,2,5,7,2,4,9,0]) == 15
assert s.maxProfit(2, [1,2,4,2,5,7,2,4,9,0]) == 13
assert s.maxProfit(3, [1,2,4,2,5,7,2,4,9,0]) == 15
assert s.maxProfit(2, [5, 4, 3, 1]) == 0


# a = [4, 6, 2, 9, 8, 10, 3]
# s.heapify(a, 0, 7)
# print(a)
assert s.maxProfit(2, [3,2,6,5,0,3]) == 7
assert s.maxProfit(1, [3,2,6,5,0,3]) == 4
# assert s.maxProfit()



# import math
#
# class Solution:
#     def maxProfit(self, k: int, prices) -> int:
#         n = len(prices)
#
#         # solve special cases
#         if not prices or k == 0:
#             return 0
#
#         # find all consecutively increasing subsequence
#         transactions = []
#         start = 0
#         end = 0
#         for i in range(1, n):
#             if prices[i] >= prices[i-1]:
#                 end = i
#             else:
#                 if end > start:
#                     transactions.append([start, end])
#                 start = i
#         if end > start:
#             transactions.append([start, end])
#
#         while len(transactions) > k:
#             # check delete loss
#             delete_index = 0
#             min_delete_loss = math.inf
#             for i in range(len(transactions)):
#                 t = transactions[i]
#                 profit_loss = prices[t[1]] - prices[t[0]]
#                 if profit_loss < min_delete_loss:
#                     min_delete_loss = profit_loss
#                     delete_index = i
#
#             # check merge loss
#             merge_index = 0
#             min_merge_loss = math.inf
#             for i in range(1, len(transactions)):
#                 t1 = transactions[i-1]
#                 t2 = transactions[i]
#                 profit_loss = prices[t1[1]] - prices[t2[0]]
#                 if profit_loss < min_merge_loss:
#                     min_merge_loss = profit_loss
#                     merge_index = i
#
#             # delete or merge
#             if min_delete_loss <= min_merge_loss:
#                 transactions.pop(delete_index)
#             else:
#                 transactions[merge_index - 1][1] = transactions[merge_index][1]
#                 transactions.pop(merge_index)
#
#         return sum(prices[j]-prices[i] for i, j in transactions)


class Solution2:

    def get_transactions(self, prices: [int]):
        transactions = []
        last_price, buy_price = float('inf'), float('inf')
        for p in prices:
            if p < last_price:
                if last_price > buy_price:
                    transactions.append((buy_price, last_price))
                buy_price = p
            last_price = p

        if last_price > buy_price:
            transactions.append((buy_price, last_price))
        return transactions


    def maxProfit(self,  k: int, prices: [int]):
        if not prices:
            return 0

        transactions = self.get_transactions(prices)
        max_profit = sum(y - x for x, y in transactions)
        if len(transactions) <= k:
            return max_profit

        n = len(transactions) - k
        while n > 0:
            i_delete = 0
            min_profit = float('inf')
            for i, (buy, sell) in enumerate(transactions):
                profit = sell - buy
                if profit < min_profit:
                    min_profit = profit
                    i_delete = i

            i_merge = 0
            min_mrg_loss = float('inf')
            for i, (buy, sell) in enumerate(transactions[:-1]):
                loss = sell - transactions[i + 1][0]
                if loss < min_mrg_loss:
                    min_mrg_loss = loss
                    i_merge = i

            if min_profit <= min_mrg_loss:
                transactions.pop(i_delete)
                max_profit -= min_profit
            else:
                transactions[i_merge] = transactions[i_merge][0], transactions[i_merge + 1][1]
                transactions.pop(i_merge + 1)
                max_profit -= min_mrg_loss

            n -= 1

        return max_profit


s = Solution2()
# assert s.maxProfit(4, [1,2,4,2,5,7,2,4,9,0]) == 15
assert s.maxProfit(2, [1,2,4,2,5,7,2,4,9,0]) == 13
assert s.maxProfit(3, [1,2,4,2,5,7,2,4,9,0]) == 15
assert s.maxProfit(2, [5, 4, 3, 1]) == 0


# a = [4, 6, 2, 9, 8, 10, 3]
# s.heapify(a, 0, 7)
# print(a)
assert s.maxProfit(2, [3,2,6,5,0,3]) == 7
assert s.maxProfit(1, [3,2,6,5,0,3]) == 4
