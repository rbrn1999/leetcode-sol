# link: https://leetcode.com/problems/wiggle-subsequence/
# better greedy solution: https://leetcode.com/problems/wiggle-subsequence/discuss/162996
class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        @cache
        def maxLen(ind: int) -> (int, int): # positive, negative direction
            if ind == 0:
                return (1, 1)

            p = n = 0
            for i in range(ind, -1, -1):
                if nums[ind] < nums[i]:
                    n = max(n, maxLen(i)[0])
                if nums[ind] > nums[i]:
                    p = max(p, maxLen(i)[1])

            return (p+1, n+1)

        return max(maxLen(len(nums)-1))
