# link: https://leetcode.com/problems/optimal-partition-of-string/

class Solution:
    def partitionString(self, s: str) -> int:
        seen = set()
        count = 1
        for c in s:
            if c in seen:
                seen = set()
                count += 1
            seen.add(c)

        return count

