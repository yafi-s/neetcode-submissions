class Solution:
    def maxProfit(self, prices: List[int]) -> int:
    
        best = 0
        left, right = 0, 1

        while right < len(prices):
            if prices[left] < prices[right]:
                diff = prices[right] - prices[left]
                best = max(diff,best)
            else:
                left = right
            right += 1
        return best
