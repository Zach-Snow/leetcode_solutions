from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        list_length = len(nums) - 1
        counter = 0
        for data in nums:
            print("data:", data)
            idx_counter = counter
            counter += 1
            print("idx_counter:", idx_counter)
            print("list_length:", list_length)
            for i in range(idx_counter, list_length):
                buffer_target = data + nums[i+1]
                print("buffer_target: ", buffer_target)
                if buffer_target == target:
                    return [int(nums.index(data)), int(i+1)]
                else:
                    pass



d = Solution()
print(d.twoSum(nums=[3,2,4], target=6))
