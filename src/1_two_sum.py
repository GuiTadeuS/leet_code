class Solution:
    def twoSum(self, nums: list, target: int) -> list:
        dictionary = {}

        for index, value in enumerate(nums):

            diferenca = target - value

            if diferenca in dictionary:
                return [dictionary[diferenca], index]
            else:
                dictionary[value] = index


nums = [2, 7, 11, 15]
target = 9

solution = Solution()
print(solution.twoSum(nums=nums, target=target))
