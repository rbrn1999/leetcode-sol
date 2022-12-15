# link: https://leetcode.com/problems/length-of-longest-fibonacci-subsequence/
# solution reference: https://leetcode.com/problems/length-of-longest-fibonacci-subsequence/solutions/152343/

from collections import defaultdict
class Solution:
    def lenLongestFibSubseq(self, arr: List[int]) -> int:
        length = {}
        nums = set(arr)
        # ...->first->second->last
        for last in range(len(arr)):
            for second in range(last):
                first_val = arr[last] - arr[second]
                if first_val < arr[second] and first_val in nums:
                    length[(arr[second], arr[last])] = length.get((first_val, arr[second]), 2) + 1
        return max(length.values()) if length else 0
