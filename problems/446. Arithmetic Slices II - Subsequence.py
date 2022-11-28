# link: https://leetcode.com/problems/arithmetic-slices-ii-subsequence/
# solution reference: https://leetcode.com/problems/arithmetic-slices-ii-subsequence/discuss/1455658/
'''
Time Complexity: O(n^2)
Space Complexity: O(n^2)
'''

class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [defaultdict(int) for _ in range(n)]

        ans = 0
        for i in range(1, n):
            for j in range(i):
                diff = nums[i] - nums[j]
                cnt = 0
                if diff in dp[j]:
                    cnt = dp[j][diff]

                dp[i][diff] += cnt + 1
                ans += cnt

        return ans
