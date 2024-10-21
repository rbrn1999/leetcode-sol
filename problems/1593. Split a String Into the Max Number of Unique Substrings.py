# link: https://leetcode.com/problems/split-a-string-into-the-max-number-of-unique-substrings/

class Solution:
    def maxUniqueSplit(self, s: str) -> int:
        used = set()
        def helper(i: int) -> int:
            if i == len(s):
                return 0
            
            count = 0
            for j in range(i+1, len(s)+1):
                if s[i:j] not in used:
                    used.add(s[i:j])
                    count = max(count, 1 + helper(j))
                    used.remove(s[i:j])
            
            return count
        
        return helper(0)
