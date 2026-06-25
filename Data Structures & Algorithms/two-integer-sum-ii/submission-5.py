class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        for i in range(len(numbers)):
            left = i + 1
            right = len(numbers) - 1
            compliment = target - numbers[i]
            while left <= right:
                middle = (left + right) // 2

                if numbers[middle] > compliment:
                    right = middle - 1
                elif numbers[middle] < compliment:
                    left = middle + 1
                else:
                    return [i + 1, middle + 1]
        return []