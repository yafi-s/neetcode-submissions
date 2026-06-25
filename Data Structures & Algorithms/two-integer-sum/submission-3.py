class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        seen = {
        }

        for i,values in enumerate(nums):
            compliment = target - values
            if compliment in seen:
                return [seen[compliment],i]
            else:
                seen[values] = i
    