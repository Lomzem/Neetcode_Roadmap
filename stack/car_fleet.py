class Solution:
    def carFleet(self, target: int, position: list[int], speed: list[int]) -> int:
        stack = []
        pos_speed = zip(position, speed)
        pos_speed = sorted(pos_speed, reverse=True)
        for pos, spd in pos_speed:
            # y = mx + b
            # x = (y - b) / m
            stack.append((target - pos) / spd)
            if len(stack) > 1:
                if stack[-1] <= stack[-2]:
                    stack.pop()

        return len(stack)

