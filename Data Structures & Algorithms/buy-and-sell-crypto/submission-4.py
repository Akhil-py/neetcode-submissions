class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        max_profit = 0
        left = 0
        right = 1

        while right < len(prices):
            profit = prices[right] - prices[left]
            if profit < 0:
                left = right
            else:
                max_profit = max(max_profit, profit)
            right += 1
            
        return max_profit
