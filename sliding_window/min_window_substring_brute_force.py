class Solution:
    def minWindow(self, s: str, t: str) -> str:
        s_map = {}
        t_map = {}
        for char in t:
            t_map[char] = t_map.get(char, 0) + 1

        l, r = 0, 0
        matches = True
        best_sub = ""
        while r < len(s):
            s_map[s[r]] = s_map.get(s[r], 0) + 1
            # print(t_map, s_map)
            for key, value in t_map.items():
                if value > s_map.get(key, 0):
                    matches = False

            if matches == True:
                if len(best_sub) > len(s[l : r + 1]) or best_sub == "":
                    best_sub = s[l : r + 1]

                l += 1
                r = l
                s_map.clear()

            else:
                r += 1
                matches = True

        return best_sub


s = "cabwefgewcwaefgcf"
t = "cae"
result = Solution().minWindow(s, t)
print(repr(result))
