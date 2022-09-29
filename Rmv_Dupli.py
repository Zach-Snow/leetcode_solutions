from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        initial_len = len(nums)

        for val in nums:
            count_occurance = nums.count(val)
            count = 1
            while count < count_occurance:
                to_pop = nums.index(val)
                nums.pop(to_pop)
                print("After pop:",nums)
                count += 1
        unique_val = len(nums)
        undr_count = initial_len - unique_val
        count = 0
        while count < undr_count:
            nums.append("_")
            count+=1
        return unique_val


d = Solution()
print(d.removeDuplicates(nums=[0,0,1,1,1,2,2,3,3,4]))
