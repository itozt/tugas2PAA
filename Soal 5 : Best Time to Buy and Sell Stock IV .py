from typing import List

class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        n = len(prices)

        if n == 0:
            return 0
        if k >= n // 2:
            max_profit = 0
            for i in range(1, n):
                if prices[i] > prices[i-1]:
                    max_profit += prices[i] - prices[i-1]
            return max_profit

        dp_buy = [-float('inf')] * (k + 1)
        dp_sell = [0] * (k + 1)

        for price in prices:
            for j in range(k, 0, -1):
                dp_sell[j] = max(dp_sell[j], dp_buy[j] + price)
                dp_buy[j] = max(dp_buy[j], dp_sell[j-1] - price)

        return max(dp_sell)
