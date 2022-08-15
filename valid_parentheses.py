class Solution:
    def isValid(self, s: str) -> bool:
        bracket_dict = {
            "(": ")",
            "{": "}",
            "[": "]"
        }
        ending_vals = []
        step = 0
        for i in range(len(s)):
            if (i + step) < len(s):
                value = s[i+step]
                for key in bracket_dict:
                    if value in bracket_dict.keys():
                        idx = s.index(s[i+step])
                        try:
                            followingVal = s[idx+1]
                            if followingVal == bracket_dict[key]:
                                step += 1
                                ending_vals.append(True)
                            elif followingVal in bracket_dict.keys():

                            else:
                                ending_vals.append(False)
                                break
                        except IndexError:
                            ending_vals.append(False)
                            break
                    elif not value:
                        pass
        final_val = list(dict.fromkeys(ending_vals))
        if len(final_val) == 1:
            return final_val[0]
        else:
            return False

d = Solution()
print(d.isValid(s="() {]"))