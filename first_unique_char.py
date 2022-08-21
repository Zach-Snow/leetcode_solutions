class Solution:
    def firstUniqChar(self, s: str) -> int:
        smallest_val = len(s)
        repeating_char_list = []
        all_char_list = []
        counter = 0
        for char in s:
            if char not in all_char_list:
                all_char_list.append(char)
            char_index = counter
            if char in repeating_char_list:
                counter += 1
                pass
            else:
                for i in range(char_index+1, len(s)):

                    if char == s[i]:
                        repeating_char_list.append(char)
                        break
                counter += 1
        for val in repeating_char_list:
            all_char_list[:] = [v for v in all_char_list if v != val]

        if not all_char_list:
            return -1

        for val in all_char_list:
            buffer_idx = s.index(val)
            if buffer_idx < smallest_val:
                smallest_val = buffer_idx
        return smallest_val

d = Solution()
print(d.firstUniqChar(s="aabb"))