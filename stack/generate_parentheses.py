class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        stack = []
        result = []

        def addParenthesis(left, right):
            if left == right == n:
                result.append(''.join(stack))
                return

            if left < n:
                stack.append('(')
                addParenthesis(left + 1, right)
                stack.pop()

            if right < left:
                stack.append(')')
                addParenthesis(left, right + 1)
                stack.pop()

        addParenthesis(0, 0)
        return result

