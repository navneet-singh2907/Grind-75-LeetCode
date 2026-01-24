def isValid(s: str) -> bool:
    stack = []
    # Map closing bracket to its opening pair
    close_to_open = {")": "(", "]": "[", "}": "{"}

    for char in s:
        if char in close_to_open:
            # It's a closing bracket
            if stack and stack[-1] == close_to_open[char]:
                stack.pop()
            else:
                return False
        else:
            # It's an opening bracket
            stack.append(char)
            
    return True if not stack else False
  
