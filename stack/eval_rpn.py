class Solution:
    def evalRPN(self, tokens: list[str]) -> int:
        operators = "+-*/"
        stack = []

        for token in tokens:
            if token not in operators:
                stack.append(int(token))
                continue

            num_2 = stack.pop()
            num_1 = stack.pop()

            match token:
                case "+":
                    stack.append(num_1 + num_2)

                case "-":
                    stack.append(num_1 - num_2)

                case "*":
                    stack.append(num_1 * num_2)

                case "/":
                    stack.append(int(num_1 / num_2))

        return stack.pop()
