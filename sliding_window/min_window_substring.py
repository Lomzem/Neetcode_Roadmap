class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # first count t
        t_count = {}
        for char in t:
            t_count[char] = t_count.get(char, 0) + 1

        have = 0
        need = t_count.__len__()  # number of keys

        left = 0
        s_count = {}

        res_left = 0
        res_right = s.__len__()
        res = ""

        for right, char in enumerate(s):
            if char in t_count.keys():  # O(26) operation
                s_count[char] = s_count.get(char, 0) + 1

                # update have
                if s_count[char] == t_count[char]:  # only want to check at, not above
                    have += 1

            while have >= need:
                if (right - left) < (res_right - res_left):
                    res_left = left
                    res_right = right
                    res = s[res_left : res_right + 1]

                # pop one from left
                if s[left] in t_count.keys():
                    s_count[s[left]] = s_count[s[left]] - 1
                    if s_count[s[left]] < t_count[s[left]]:
                        have -= 1

                left += 1

        return res
