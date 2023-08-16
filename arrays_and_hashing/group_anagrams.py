# original memory idea: keys = dict counter/pattern, values = list that match that pattern

# first solution

# class Solution:
#     def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
#         string_patterns = {}
#
#         for string in strs:
#             chars_array = [0] * 26
#
#             for char in string:
#                 letter_index = ord(char) - ord('a')
#                 chars_array[letter_index] = chars_array[letter_index] + 1
#
#             chars_tuple = tuple(chars_array)
#             if chars_tuple not in string_patterns:
#                 string_patterns[chars_tuple] = []
#
#             string_patterns[chars_tuple].append(string)
#
#         return list(string_patterns.values())





# answer after learning about defaultdicts

import collections

class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        string_patterns = collections.defaultdict(list)

        for string in strs:
            chars_counter = [0] * 26

            for char in string:
                chars_counter[ord(char) - ord('a')] += 1

            string_patterns[tuple(chars_counter)].append(string)

        return list(string_patterns.values())





# solution that incorporates sorted()

# import collections
#
# class Solution:
#     def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
#         string_patterns = collections.defaultdict(list)
#         for string in strs:
#             pattern = tuple(sorted(*[string]))
#             string_patterns[pattern].append(string)
#
#         return list(string_patterns.values())

