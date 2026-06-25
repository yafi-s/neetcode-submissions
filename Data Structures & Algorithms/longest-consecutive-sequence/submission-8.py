class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
 
        setNum = set(nums)
        best = 0

        if len(setNum) == 1:
            return 1
    #in our set there is a number n - 1 we want to find the beginning of the sequence
    # streak = 1, n + 1 exist, return the greatest streka 

        for n in setNum:
            if n - 1 in setNum:
                continue 
            streak = 1
            while n + streak in setNum:
                streak += 1
                best = max(best,streak)
        return best