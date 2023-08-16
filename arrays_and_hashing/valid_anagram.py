# First solution: slower because loops over both s and t

# class Solution:
#     def count_chars(self, string: str) -> dict:
#         counter = {}
#         for char in string:
#             counter[char] = counter.get(char, 0) + 1
#         return counter
#
#     def isAnagram(self, s: str, t: str) -> bool:
#         if len(s) != len(t):
#             return False

#         return self.count_chars(s) == self.count_chars(t)

# Updated solution: only has to loop over s because s and t have same length

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        counter_s = {}
        counter_t = {}

        for i in range(len(s)):
            counter_s[s[i]] = counter_s.get(s[i], 0) + 1
            counter_t[t[i]] = counter_t.get(t[i], 0) + 1

        return counter_s == counter_t
