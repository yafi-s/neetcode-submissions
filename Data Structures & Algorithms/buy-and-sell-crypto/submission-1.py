class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        best = 0
        buy = 0
        sell = 1

        while sell < len(prices):
            if prices[buy] < prices[sell]:
                best = max(best, prices[sell] - prices[buy])
            else:
                buy = sell
            sell += 1
        return best
