# link: https://leetcode.com/problems/numbers-with-same-consecutive-differences/

class Solution:
    def numsSameConsecDiff(self, n: int, k: int) -> List[int]:
        result = []
        def dfs(v):
            if len(v) == n:
                result.append(v)
                return

            if int(v[-1]) + k < 10:
                dfs(v+str(int(v[-1])+k))
            if k != 0 and int(v[-1])-k >= 0:
                dfs(v+str(int(v[-1])-k))

        for i in range(1, 10):
            dfs(str(i))
        return result
