class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        NumSet = set(nums)
        streak = 0
        best = 0

        for n in NumSet:
            if n - 1 not in NumSet:
                streak = 1
                while n + streak in NumSet:
                    streak += 1
                best = max(best,streak)
        return best