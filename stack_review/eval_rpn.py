class Solution:
    def evalRPN(self, tokens: list[str]) -> int:
        stack = []
        for token in tokens:
            if not token in '+-*/':
                stack.append(token)
                continue

            num_1 = int(stack.pop())
            num_2 = int(stack.pop())

            match token:
                case '+':
                    stack.append(num_1 + num_2)
                case '-':
                    stack.append(num_2 - num_1)
                case '*':
                    stack.append(num_1 * num_2)
                case '/':
                    stack.append(int(num_2) / num_1)

        return int(stack.pop())
