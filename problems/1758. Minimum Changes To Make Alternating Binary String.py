# link: https://leetcode.com/problems/minimum-changes-to-make-alternating-binary-string/

class Solution:
    def minOperations(self, s: str) -> int:
        op_count = 0
        prev = s[0]
        for c in s[1:]:
            if c == prev:
                op_count += 1
            prev = '1' if prev == '0' else '0'
        
        ans = op_count
        op_count = 1
        prev = '1' if s[0] == '0' else '0'
        for c in s[1:]:
            if c == prev:
                op_count += 1
            prev = '1' if prev == '0' else '0'
        ans = min(ans, op_count)
        return ans