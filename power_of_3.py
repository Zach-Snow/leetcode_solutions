class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n < 3 and n != 1:
            return False
        else:
            val = n
            while val >= 3:
                val = val / 3
            if val < 3 and val == 1:
                return True
            else:
                return False

d = Solution()
print(d.isPowerOfThree(n=1))
