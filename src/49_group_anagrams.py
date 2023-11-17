class Solution:

    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        dictionary = dict()
        for letter_s in s:
            if letter_s in dictionary:
                dictionary[letter_s] += 1
            else:
                dictionary[letter_s] = 1
        for letter_t in t:
            if letter_t in dictionary:
                dictionary[letter_t] -= 1
        for value in dictionary.values():
            if value != 0:
                return False
        return True

    def groupAnagrams(self, strs: list) -> list:

        for index_i, value_i in enumerate(strs):
            for index_j, value_j in enumerate(strs):
                if index_i+1 < len(strs):
                    print(self.isAnagram(strs[index_i], strs[index_j]))


solution = Solution()
strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
solution.groupAnagrams(strs=strs)
