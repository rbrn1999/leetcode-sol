# link: https://leetcode.com/problems/russian-doll-envelopes/
# solution: https://leetcode.com/problems/russian-doll-envelopes/discuss/1134011/JS-Python-Java-C%2B%2B-or-Easy-LIS-Solution-w-Explanation

from bisect import bisect_left
class Solution:
    def maxEnvelopes(self, envelopes: list[list[int]]) -> int:
        envelopes = sorted(envelopes, key= lambda x: (x[0], -x[1]))
        
        sub = []
        for _, h in envelopes:
            if not sub or sub[-1] < h:
                sub.append(h)
            else:
                idx = bisect_left(sub, h)
                sub[idx] = h
        return len(sub)