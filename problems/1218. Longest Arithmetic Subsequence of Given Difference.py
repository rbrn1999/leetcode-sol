# link: https://leetcode.com/problems/longest-arithmetic-subsequence-of-given-difference/

class Solution:
    def longestSubsequence(self, arr: List[int], difference: int) -> int:
        prev = {}
        for num in arr:
            if num-difference in prev:
                prev[num] = max(prev.get(num, 0), prev[num-difference]+1)
            else:
                prev.setdefault(num, 1)

        return max(prev.values())

