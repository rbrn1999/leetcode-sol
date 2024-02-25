# link: https://leetcode.com/problems/least-number-of-unique-integers-after-k-removals

from collections import defaultdict

class Solution:
    def findLeastNumOfUniqueInts(self, arr: list[int], k: int) -> int:
        num_count = defaultdict(int)
        for num in arr:
            num_count[num] += 1
        
        freq_count = defaultdict(int)
        for num in num_count:
            freq_count[num_count[num]] += 1
        
        freqs = sorted(freq_count.keys())
        res = len(num_count.keys())
        i = 0
        while i < len(freqs) and k >= 0:
            if freqs[i] * freq_count[freqs[i]] <= k:
                res -= freq_count[freqs[i]]
                k -= freqs[i] * freq_count[freqs[i]]
                i += 1
            else:
                res -= k // freqs[i]
                break
            
        
        return res