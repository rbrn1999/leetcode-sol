class Solution:
    def climbStairs(self, n: int) -> int:
        result = [0] * (n+1)
        result[:2] = [1, 1]
        #two ways to climb from result[n-2] to result[n] (1+1) or (2)
        #one way to climb from result[n-1] to result[n] (1)
        for i in range(3, n+1):
            result[i] = result[i-1] + result[i-2]
        return result[n]