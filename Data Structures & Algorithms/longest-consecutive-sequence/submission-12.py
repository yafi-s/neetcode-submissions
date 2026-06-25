class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        streak = 0
        nums_set = set(nums)
        for n in nums:
            if n - 1 in nums_set:
                continue
            else:
                curr = 1
                while n + 1 in nums_set:
                    curr += 1
                    n += 1
                streak = max(streak,curr)
        return streak
