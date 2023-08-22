class Solution:
    def encode(self, strs):
        result = ''
        for item in strs:
            result += f'{len(item)}#{item}'
        return result

    def decode(self, str):
        beg_pointer = 0
        end_pointer = 0

        result = []

        while beg_pointer < len(str):
            if str[end_pointer] == '#':
                count = int(str[beg_pointer : end_pointer])
                result.append(str[end_pointer + 1 : end_pointer + count + 1])
                beg_pointer = end_pointer + count + 1
                end_pointer = end_pointer + count + 1

            end_pointer += 1

        return result

