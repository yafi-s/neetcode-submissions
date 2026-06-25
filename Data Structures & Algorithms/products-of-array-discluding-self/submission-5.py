class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        prefix = 1
        res = [1] * len(nums)

        for n in range(len(nums)):
            res[n] = prefix
            prefix *= nums[n]

        postfix = 1

        for n in range(len(nums)-1,-1,-1):
            res[n] *= postfix
            postfix *= nums[n]

        return res