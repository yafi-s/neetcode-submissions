class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        for i in range(len(numbers)):
            left,right = i + 1, len(numbers) - 1
            while left <= right:
                compliment = target - numbers[i]
                middle = left + (right - left) // 2
                if numbers[middle] == compliment:
                    return[i+1,middle+1]
                elif numbers[middle] < compliment:
                    left = middle + 1
                else:
                    right = middle - 1