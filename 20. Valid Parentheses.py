class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        mapping = {')': '(', ']': '[', '}': '{'}
        
        for char in s:
            if char in mapping:  # If it's a closing bracket
                top_element = stack.pop() if stack else '#'  # Pop or use placeholder if empty
                if mapping[char] != top_element:
                    return False
            else:
                stack.append(char)  # Push opening brackets
        
        return not stack  # Valid if stack is empty at the end
