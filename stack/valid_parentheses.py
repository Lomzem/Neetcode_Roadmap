class Solution:
    def isValid(self, s: str) -> bool:
        closing_pairs = {']': '[', '}': '{', ')': '('}
        stack = []

        for char in s:
            if char not in closing_pairs.keys():
                stack.append(char)
            elif stack and closing_pairs[char] == stack[-1]:
                stack.pop()
            else:
                return False

        return False if stack else True
