from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # Inicializando
        n = len(nums)
        prefix = 1
        postfix = 1
        answer = [1] * n

        for index in range(n):
            answer[index] = prefix
            prefix *= nums[index]

        for index in range(n - 1, -1, -1):
            answer[index] *= postfix
            postfix *= nums[index]

        return answer


solution = Solution()
nums = [-1, 1, 0, -3, 3]
print(solution.productExceptSelf(nums))
