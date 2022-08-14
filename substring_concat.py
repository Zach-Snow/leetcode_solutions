from typing import List
import re
from itertools import chain, permutations


class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        data = list(chain.from_iterable([permutations(words, x) for x in range(len(words) + 1)]))
        longest_combination = 0
        list_combo = []
        position_list = []
        for val in data:
            length_val = len(val)
            if length_val > longest_combination:
                longest_combination = length_val
        for val in data:
            length_val = len(val)
            string = ""
            if length_val == longest_combination:
                for combo in val:
                    string = string + combo
                list_combo.append(string)

        # singular string check
        first_val = list_combo[0][0]
        flag = True
        counter = 0
        idx = []
        list_combo_len = len(list_combo)
        for val in list_combo:
            counter += 1
            if len(val) > len(s):
                return []
            else:
                for char in val:
                    if char == first_val:
                        flag = True
                        list_combo = list(dict.fromkeys(list_combo))
                    elif char != first_val:
                        flag = False
                if flag:
                    string_flag = all(elem == s[0] for elem in s)
                    if string_flag and s[0] == first_val:
                        ignore_index = len(list_combo[0]) - 1
                        ret_list = []
                        len_s = len(s)
                        if len_s == 1:
                            ret_list.append(int(0))
                        else:
                            for x in range(0, len_s - ignore_index):
                                ret_list.append(int(x))
                        return ret_list
                    elif not string_flag:
                        value = [m.start() for m in re.finditer(f'(?={val})', s)]
                        if not value:
                            pass
                        else:
                            for dat in value:
                                idx.append(dat)
                        if counter < list_combo_len:
                            pass
                        else:
                            idx = list(dict.fromkeys(idx))
                            return idx
                elif not flag:
                    ret_list = []
                    pattern_flag = True
                    for pattern in list_combo:
                        main_string_len = len(s)
                        pattern_length = len(pattern)
                        primary = ""
                        offset = 0
                        for i in range(offset, pattern_length):
                            primary = primary + s[i]
                        ret_list.append(int(offset))
                        main_pat_len = len(primary)
                        offset = main_string_len - main_pat_len
                        secondary = ""
                        if (pattern_length + offset) <= len(s):
                            for i in range(offset, pattern_length + offset):
                                secondary = secondary + s[i]
                        if primary == secondary == pattern:
                            ret_list.append(int(offset))
                        else:
                            pattern_flag = False
                    if pattern_flag:
                        return ret_list
                    elif not pattern_flag:
                        for combination in list_combo:
                            # index = [_.start() for _ in re.finditer(combination, s)]
                            index = [m.start() for m in re.finditer(f'(?={combination})', s)]
                            if index == -1:
                                pass
                            else:
                                for idx in index:
                                    position_list.append(int(idx))
                        final_list = list(dict.fromkeys(position_list))
                        return final_list


d = Solution()
print(d.findSubstring(s="aaaccccaab", words=["cc", "cc"]))

# This is the actual solve, above one is a more complicated way I was trying
# from collections import Counter, defaultdict
#
#
# class Solution:
#
#     def findSubstring(self, s: str, words: List[str]) -> List[int]:
#         length = len(words[0])
#         word_count = Counter(words)
#         indexes = []
#
#         for i in range(length):
#             start = i
#             window = defaultdict(int)
#             words_used = 0
#
#             for j in range(i, len(s) - length + 1, length):
#                 word = s[j:j + length]
#
#                 if word not in word_count:
#                     start = j + length
#                     window = defaultdict(int)
#                     words_used = 0
#                     continue
#
#                 words_used += 1
#                 window[word] += 1
#
#                 while window[word] > word_count[word]:
#                     window[s[start:start + length]] -= 1
#                     start += length
#                     words_used -= 1
#
#                 if words_used == len(words):
#                     indexes.append(start)
#
#         return indexes
