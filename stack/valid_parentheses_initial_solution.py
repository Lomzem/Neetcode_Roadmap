class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) == 1:
            return False

        stack = []
        opening = '([{'
        pairs = {')': '(', ']': '[', '}': '{'}

        for char in s:
            if len(stack) == 0 and char not in opening:
                return False

            if char in opening:
                stack.append(char)

            else:
                if pairs[char] == stack[-1]:
                    stack.pop()
                else:
                    return False

        return len(stack) == 0
