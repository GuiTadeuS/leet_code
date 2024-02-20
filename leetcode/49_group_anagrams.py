from collections import defaultdict


class Solution:
    def groupAnagrams(self, strs):
        anagram_map = defaultdict(list)

        for palavra in strs:
            sorted_word = str(sorted(palavra))
            anagram_map[sorted_word].append(palavra)

        return list(anagram_map.values())


solution = Solution()
strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
print(solution.groupAnagrams(strs=strs))
