# link: https://leetcode.com/problems/minimum-deletions-to-make-string-balanced/

class Solution:
    def minimumDeletions(self, s: str) -> int:
        minCount = float('inf')
        n = len(s)
        aCount = []
        cur_count = 0
        for char in s:
            if char == 'a':
                cur_count += 1
            aCount.append(cur_count)

        result = n
        # edge case: whole string is b portion
        result = min(result, aCount[n-1])
        for i in range(n): # i: 0~i: a portion (inclusive)
            cur_delete_count = (i + 1 - aCount[i]) + (aCount[n-1] - aCount[i])
            result = min(result, cur_delete_count)

        return result

