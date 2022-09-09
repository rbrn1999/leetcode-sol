# link: https://leetcode.com/problems/calculate-digit-sum-of-a-string/
class Solution:
    def digitSum(self, s: str, k: int) -> str:
        def compress(s):
            return str(sum(int(c) for c in s))
        
        while len(s) > k:
            nextS = ''.join(compress(s[i:i+k]) for i in range(0, len(s)-k+1, k))
            if len(s) % k != 0:
                nextS += compress(s[-(len(s)%k):])
            s = nextS

        return s

print(Solution().digitSum("11111222223", 3))