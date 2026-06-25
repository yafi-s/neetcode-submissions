class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        seen = {}
        for i,value in enumerate(numbers):
            compliment = target - value
            if compliment in seen:
                return [seen[compliment] + 1,i + 1]  
            seen[value] = i 
