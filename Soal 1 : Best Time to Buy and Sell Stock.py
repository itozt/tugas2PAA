from typing import List

class Solution: 
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:  
            return 0

        min_price = float('inf') 
        max_profit = 0            

        for price in prices:
            if price < min_price:
                min_price = price
            else:
                max_profit = max(max_profit, price - min_price)

        return max_profit

if __name__ == "__main__":
    s = Solution()

