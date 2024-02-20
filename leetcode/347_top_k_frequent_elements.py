from collections import defaultdict
from typing import List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequency_map = defaultdict(int)

        for number in nums:
            frequency_map[number] += 1

        answer = []
        while len(answer) < k and frequency_map:
            max_key = max(frequency_map, key=frequency_map.get)
            answer.append(max_key)
            del frequency_map[max_key]

        return answer


solution = Solution()
nums = [1, 1, 1, 2, 2, 3]
k = 2
print(solution.topKFrequent(nums, k))
