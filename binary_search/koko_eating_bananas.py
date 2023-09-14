class Solution:
    def minEatingSpeed(self, piles: list[int], h: int) -> int:
        left = 1
        right = max(piles)

        while left <= right:
            k = (left + right) // 2
            total_time = 0
            for pile in piles:
                total_time += 
