class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
    # Input: nums, target 
    # Process  two numberse from the array that adds up to the target 
    # 
    # Output list(index, index)

        numbers = {}

        for i,value in enumerate(nums):
            diff = target - value
            if diff in numbers:
                return [numbers[diff],i]
            else:
                numbers[value] = i
