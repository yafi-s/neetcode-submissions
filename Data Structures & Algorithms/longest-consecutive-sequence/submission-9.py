class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
 
        numSet = set(nums)
        best = 0
        
        for n in numSet:
            if n - 1 in numSet:
                continue
            else:
                streak = n
                curr = 1
                while streak + 1 in numSet:
                    streak += 1
                    curr += 1
                best = max(curr,best)

        return best