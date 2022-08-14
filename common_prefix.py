from typing import List
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        latest_pattern = ""
        counter = 0
        for char in strs:
            if not latest_pattern and counter == 0:
                latest_pattern = char
                counter += 1
            else:
                buffer_pattern = ""
                if len(char) < len(latest_pattern):
                    for i in range(len(char)):
                        if char[i] == latest_pattern[i]:
                            buffer_pattern = buffer_pattern + char[i]
                        else:
                            break
                else:
                    for i in range(len(latest_pattern)):
                        if char[i] == latest_pattern[i]:
                            buffer_pattern = buffer_pattern + char[i]
                        else:
                            break
                if not buffer_pattern:
                    latest_pattern = ""
                else:
                    latest_pattern = buffer_pattern
                counter += 1

        return latest_pattern








d = Solution()
print(d.longestCommonPrefix(strs=["cir","car"]))

