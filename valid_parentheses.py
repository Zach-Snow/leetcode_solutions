class Solution:
    def isValid(self, s: str) -> bool:
        bracket_dict = {
            "(": ")",
            "{": "}",
            "[": "]"
        }

        latest_list = []
        for char in s:
            last_pos = len(latest_list) - 1
            if char not in bracket_dict.keys():
                try:
                    if char == bracket_dict[latest_list[last_pos]]:
                        latest_list.pop(last_pos)
                    else:
                        return False
                except IndexError:
                    latest_list.append(char)
                except KeyError:
                    return False
            elif char in bracket_dict.keys():
                latest_list.append(char)

        if not latest_list:
            return True
        else:
            return False


d = Solution()
print(d.isValid(s="))"))
