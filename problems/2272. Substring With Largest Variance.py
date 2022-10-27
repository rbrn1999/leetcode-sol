# link: https://leetcode.com/problems/substring-with-largest-variance/submissions/
# solutin reference: https://leetcode.com/problems/substring-with-largest-variance/discuss/2039178/

class Solution:
    def largestVariance(self, s: str) -> int:
        # Kadane’s Algorithm
        def largestSub(c1, c2):
            cur_var = max_var = 0
            has_c2 = False
            c2_at_first = False
            for c in s:
                cur_var += 1 if c == c1 else 0
                if c == c2:
                    has_c2 = True
                    if c2_at_first and cur_var >= 0:
                        c2_at_first = False
                    else:
                        cur_var -= 1
                        if cur_var < 0: # reset start point
                            c2_at_first = True
                            cur_var = -1   
                
                if has_c2:
                    max_var = max(max_var, cur_var)

            return max_var
        
        res = 0
        chars = set(s)
        for c1 in chars:
            for c2 in chars:
                if c1 == c2:
                    continue
                res = max(res, largestSub(c1, c2))
        return res
