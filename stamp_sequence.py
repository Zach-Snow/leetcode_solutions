from typing import List


class Solution:
    def movesToStamp(self, stamp: str, target: str) -> List[int]:
        step = len(stamp) - 1
        print("step:", step)
        ret_list = []
        iterate_flag = True

        if len(stamp) > len(target):
            return []
        else:
            s = []
            for i in range(len(target)):
                s.append("?")
        last_val = 0
        starting_index = 0
        while iterate_flag:
            for i in range(starting_index, len(target)):
                if len(target)-starting_index < len(stamp):
                    iterate_flag = False
                else:
                    try:
                        s[i] = stamp[i]
                        if starting_index not in ret_list:
                            ret_list.append(starting_index)
                            last_val = i
                    except IndexError:
                        pass
            print("last_val:", last_val)
            starting_index += step

        return ret_list

# class Solution:
#     def movesToStamp(self, stamp: str, target: str) -> List[int]:
#         if stamp == target: return [0]
#         S, T = list(stamp), list(target)
#         slen, tlen = len(S), len(T) - len(S) + 1
#         ans, tdiff, sdiff = [], True, True
#         while tdiff:
#             tdiff = False
#             for i in range(tlen):
#                 sdiff = False
#                 for j in range(slen):
#                     if T[i + j] == "?": continue
#                     if T[i + j] != S[j]: break
#                     sdiff = True
#                 else:
#                     if sdiff:
#                         tdiff = True
#                         for j in range(i, i + slen): T[j] = "?"
#                         ans.append(i)
#         for i in range(len(T)):
#             if T[i] != "?": return []
#         return reversed(ans)


d = Solution()
print(d.movesToStamp(stamp="abca", target="aabcaca"))
