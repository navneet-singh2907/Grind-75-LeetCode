class Solution:
    def evalRPN(self, tokens):
        stack = []
        
        for t in tokens:
            if t == "+":
                stack.append(stack.pop() + stack.pop())
            elif t == "-":
                b, a = stack.pop(), stack.pop()
                stack.append(a - b)
            elif t == "*":
                stack.append(stack.pop() * stack.pop())
            elif t == "/":
                b, a = stack.pop(), stack.pop()
                # Explicit float division cast to int for zero-truncation
                stack.append(int(float(a) / b))
            else:
                stack.append(int(t))
                
        return stack[0]
