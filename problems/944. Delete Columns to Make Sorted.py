# link: https://leetcode.com/problems/delete-columns-to-make-sorted/

class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        n, m = len(strs), len(strs[0])
        count = 0
        for col in range(m):
            for row in range(n-1):
                if strs[row][col] > strs[row+1][col]:
                    count += 1
                    break

        return count

