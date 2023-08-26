# First O(n^2) solution of brute force
# class Solution:
#     def maxArea(self, height: list[int]) -> int:
#         max_area = 0
#
#         for i, bar in enumerate(height):
#             for j in range(i, len(height)):
#                 y_cap = min(bar, height[j])
#                 length = j - i
#                 area = y_cap * length
#                 max_area = max(max_area, area)
#
#         return max_area

class Solution:
    def maxArea(self, height: list[int]) -> int:
        left = 0
        right = len(height) - 1
        max_area = 0

        while left < right:
            length = right - left
            width = min(height[left], height[right])
            area = length * width
            max_area = max(max_area, area)

            if height[left] <= height[right]:
                left += 1
            elif height[left] > height[right]:
                right -= 1

        return max_area
