from collections import deque
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = deque()

        for t in tokens:
            if t in {"+", "-", "*", "/"}:
                b = stack.pop()   
                a = stack.pop()   

                if t == "+":
                    stack.append(a + b)
                elif t == "-":
                    stack.append(a - b)
                elif t == "*":
                    stack.append(a * b)
                else:  
                    stack.append(int(a / b))  # truncate toward zero
            else:
                stack.append(int(t))

        return stack[0]
