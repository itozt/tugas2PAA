from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices or len(prices) < 2:
            return 0
        hold_profit = -prices[0]
        sold_profit = float('-inf')
        rest_profit = 0

        for i in range(1, len(prices)):
            current_price = prices[i]

            prev_hold_profit = hold_profit
            prev_sold_profit = sold_profit
            prev_rest_profit = rest_profit

            hold_profit = max(prev_hold_profit, prev_rest_profit - current_price)
            sold_profit = prev_hold_profit + current_price
            rest_profit = max(prev_sold_profit, prev_rest_profit)

        return max(sold_profit, rest_profit)
