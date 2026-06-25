class Solution:
    def maxProfit(self, prices: List[int]) -> int:
    

        best = 0
        left, right = 0, 1

        while right < len(prices):
            if prices[right] < prices[left]:
                left = right
            else:
                diff = prices[right] - prices[left]
                best = max(best, diff)
            right += 1
        return best