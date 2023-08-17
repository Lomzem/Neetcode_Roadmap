# from memory

class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        counter = {}
        for num in nums:
            counter[num] = counter.get(num, 0) + 1

        occurrences = [[] for i in range(len(nums) + 1)]
        for num, count in counter.items():
            occurrences[count].append(num)

        result = []
        for count in range(len(occurrences) - 1, 0, -1):
            for num in occurrences[count]:
                result.append(num)
                if len(result) == k:
                    return result
