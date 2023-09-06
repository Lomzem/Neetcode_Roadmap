class Solution:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        up, down = 0, len(matrix) - 1

        while up <= down:
            mid_v = (up + down) // 2
            if matrix[mid_v][0] > target:
                down = mid_v - 1
            elif matrix[mid_v][-1] < target:
                up = mid_v + 1
            else:
                left, right = 0, len(matrix[mid_v]) - 1
                while left <= right:
                    mid_h = (left + right) // 2
                    if matrix[mid_v][mid_h] > target:
                        right = mid_h - 1
                    elif matrix[mid_v][mid_h] < target:
                        left = mid_h + 1
                    else:
                        # return matrix[mid_v][mid_h]
                        return True
                return False

