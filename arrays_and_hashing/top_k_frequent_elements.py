import collections

class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        counter = {}

        # count the number of occurrences of each num
        for num in nums:
            counter[num] = counter.get(num, 0) + 1

        # make the number of occurrences the key in a dict, and the original num the value of the dict
        # since multiple nums could have the same count, the values are stored in a list
        sorted_counter = collections.defaultdict(list)
        for key in counter:
            sorted_counter[counter[key]].append(key)

        # sort the keys (occurences) in our list in reverese so we
        # could access it using k as index
        keys_list = sorted(list(sorted_counter.keys()), reverse=True)
        sorted_counter = {key: sorted_counter[key] for key in keys_list}

        sorted_values = list(sorted_counter.values())[:k]

        # deal with the issue of multiple nums having same occurence and only returning k nums
        flat_list = [in_list_item for in_list in sorted_values for in_list_item in in_list]
        return flat_list[:k]

