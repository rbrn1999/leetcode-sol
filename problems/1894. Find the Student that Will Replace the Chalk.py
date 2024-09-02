# link: https://leetcode.com/problems/find-the-student-that-will-replace-the-chalk/

class Solution:
    def chalkReplacer(self, chalk: list[int], k: int) -> int:
        chalks_per_round = sum(chalk)
        k %= chalks_per_round

        print(k)
        for i in range(len(chalk)):
            if chalk[i] > k:
                return i
            else:
                k -= chalk[i]
        
        return -1