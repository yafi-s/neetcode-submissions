class Solution:
 def hasDuplicate(self, nums: List[int]) -> bool:
        
    solution = set();

    for i in nums:
        if i in solution:
            return True
        else:
            solution.add(i)
    return False