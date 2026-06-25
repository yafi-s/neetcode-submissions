class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        ans = {}

        for idx, value in enumerate(nums):
            compliment = target - value
            if compliment in ans:
                return [ans[compliment], idx]
            ans[value] = idx

        