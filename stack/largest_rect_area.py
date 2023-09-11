class Solution:
    def largestRectangleArea(self, heights: list[int]) -> int:
        stack = []
        max_area = 0

        for i, height in enumerate(heights):
            if stack and height < heights[stack[-1]]:
                p_index = stack.pop()
                area = (i - p_index) * heights[p_index]
                max_area = max(max_area, area)
                stack.append(p_index)

            stack.append(i)

        return max_area
        
Solution().largestRectangleArea(heights = [2,1,5,6,2,3])
