class Solution:
    def trap(self, height: list[int]) -> int:
        left = 0
        right = len(height) - 1

        max_left = height[left]
        max_right = height[right]

        water_count = 0

        while left < right:
            if height[left] <= height[right]:
                left += 1
                max_left = max(max_left, height[left])
                water_possible = min(max_left, max_right) - height[left]
                print((left, right, max_left, max_right, water_possible))
                if water_possible > 0:
                    water_count += water_possible
            else:
                right -= 1
                max_right = max(max_right, height[right])
                water_possible = min(max_left, max_right) - height[right]
                if water_possible > 0:
                    water_count += water_possible

        return water_count

