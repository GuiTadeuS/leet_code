class Solution:
    def isPalindrome(self, x: int) -> bool:
        x = str(x)
        reverse_x = x[::-1] # simple slicing - goes backward slicing [start:end:step]

        if x == reverse_x:
            return True
        return False
solution = Solution()
x = 12
print(solution.isPalindrome(x))