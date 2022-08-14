class Solution:
    def romanToInt(self, s: str) -> int:
        ret_val = 0
        iteration_pass = []
        index = len(s)-1
        for i in range(0, len(s)):
            iteration_pass.append(False)

        for val in reversed(s):
            compare_val = s[index - 1]
            if index == 0:
                compare_val = "end"
            if iteration_pass[index]:
                pass
            else:
                if val == "I":
                    ret_val += 1
                elif val == "V" and compare_val == "I":
                    ret_val += 4
                    iteration_pass[index] = True
                    iteration_pass[index - 1] = True
                elif val == "V" and compare_val != "I":
                    ret_val += 5
                    iteration_pass[index] = True
                elif val == "X" and compare_val == "I":
                    ret_val += 9
                    iteration_pass[index] = True
                    iteration_pass[index - 1] = True
                elif val == "X" and compare_val != "I":
                    ret_val += 10
                    iteration_pass[index] = True
                elif val == "L" and compare_val == "X":
                    ret_val += 40
                    iteration_pass[index] = True
                    iteration_pass[index - 1] = True
                elif val == "L" and compare_val != "X":
                    ret_val += 50
                    iteration_pass[index] = True
                elif val == "C" and compare_val == "X":
                    ret_val += 90
                    iteration_pass[index] = True
                    iteration_pass[index - 1] = True
                elif val == "C" and compare_val != "X":
                    ret_val += 100
                    iteration_pass[index] = True
                elif val == "D" and compare_val == "C":
                    ret_val += 400
                    iteration_pass[index] = True
                    iteration_pass[index - 1] = True
                elif val == "D" and compare_val != "C":
                    ret_val += 500
                    iteration_pass[index] = True
                elif val == "M" and compare_val == "C":
                    ret_val += 900
                    iteration_pass[index] = True
                    iteration_pass[index - 1] = True
                elif val == "M" and compare_val != "C":
                    ret_val += 1000
                    iteration_pass[index] = True
            index -= 1

        return ret_val


d = Solution()
print(d.romanToInt("MMMCDXC")) #MMMMMMDCCCLXXXI
