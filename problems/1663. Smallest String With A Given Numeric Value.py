# link: https://leetcode.com/problems/smallest-string-with-a-given-numeric-value/

class Solution:
    def getSmallestString(self, n: int, k: int) -> str:
        k -= n
        z_count = k // 25
        r = k % 25
        return 'a'*(n - z_count - 1) + ('' if z_count == n else chr(97 + r)) + 'z' * z_count


print(Solution().getSmallestString(5, 130))
