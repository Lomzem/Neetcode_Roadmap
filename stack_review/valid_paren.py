class Solution:
    def isValid(self, s: str) -> bool:
        pairs = {'}': '{', ']': '[', ')': '('}
        stack = [] 
        for char in s:
            if char in '([{':
                stack.append(char)
                continue

            if not stack or stack[-1] != pairs[char]:
                return False

            stack.pop()
        
        return False if stack else True

            
