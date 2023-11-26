from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        answer = []
        for index_x, value_x in enumerate(nums):
            stash = []
            result = 1
            for index_y, value_y in enumerate(nums):
                if index_x != index_y:
                    stash.append(value_y)
            for value in stash:
                result = result * value
            answer.append(result)
        return answer


solution = Solution()
nums = [-1, 1, 0, -3, 3]
print(solution.productExceptSelf(nums))
