class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        if nums == []:
            return False
        dictionary = {}
        for number in nums:
            if number in dictionary:
                return True
            else:
                dictionary[number] = 1
        return False
