class Solution:
    def calculate(self, s: str) -> int:
        stack = []
        num = 0
        res = 0
        sign = 1 # 1 for positive, -1 for negative
        
        i = 0
        while i < len(s):
            char = s[i]
            
            if char.isdigit():
                # Form the full number
                num = 0
                while i < len(s) and s[i].isdigit():
                    num = num * 10 + int(s[i])
                    i += 1
                res += sign * num
                # Continue because the outer while handles increment
                continue
            
            elif char == '+':
                sign = 1
            elif char == '-':
                sign = -1
            elif char == '(':
                # Save the current result and sign to the stack
                stack.append(res)
                stack.append(sign)
                # Reset for the new scope inside ()
                res = 0
                sign = 1
            elif char == ')':
                # Apply the sign to the current result inside ()
                res *= stack.pop()
                # Add the result before the parenthesis started
                res += stack.pop()
                
            i += 1
            
        return res
