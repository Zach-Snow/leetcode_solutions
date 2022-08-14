class Solution:
    def isPalindrome(self, x: int) -> bool:
        true_val = str(x)
        revarsed_val = true_val[::-1]
        if true_val == revarsed_val:
            return True
        else:
            return False

d = Solution()
print(d.isPalindrome(221221))