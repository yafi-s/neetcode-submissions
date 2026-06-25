from collections import deque
class Solution:
    def isValid(self, s: str) -> bool:
        
        
        isValid = {']': '[', '}' : '{', ')':'(' }
        stack = deque()

        for c in s:
            if c in isValid:
                if stack and stack[-1] == isValid[c]:
                    stack.pop()
                else:
                     return False
            else:
                stack.append(c)

        return not stack   
            

