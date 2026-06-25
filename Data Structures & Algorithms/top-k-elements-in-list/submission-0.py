from collections import defaultdict
import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        seen = defaultdict(int)

        for n in nums:
            seen[n] += 1
        
        largest_keys = heapq.nlargest(k, seen, key=seen.get)
        return largest_keys