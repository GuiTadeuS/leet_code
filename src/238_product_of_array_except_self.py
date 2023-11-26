from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        answer = []
        for index, value in enumerate(nums):
            if nums[index] != value:
                result = nums[index]


solution = Solution()
nums = [1, 2, 3, 4]
# print(len(nums))
print(solution.productExceptSelf(nums))
