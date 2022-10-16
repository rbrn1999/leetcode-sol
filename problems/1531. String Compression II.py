# link: https://leetcode.com/problems/string-compression-ii/
# solution reference: https://leetcode.com/problems/string-compression-ii/discuss/767602/

from functools import cache
class Solution:
    def getLengthOfOptimalCompression(self, s: str, k: int) -> int:
        @cache
        def helper(i, curr_streak_char, streak_len, remain_dels):
            if i == len(s):
                return 0
            
            # 2 choices: keep or delete the current char
            
            # keep
            keep_curr_cost = 0
            if s[i] == curr_streak_char:
                extra_digit_count = 0
                if streak_len == 1 or len(str(streak_len+1)) > len(str(streak_len)):
                    extra_digit_count = 1
                keep_curr_cost = extra_digit_count + helper(i+1, curr_streak_char, streak_len+1, remain_dels)
            else:
                keep_curr_cost = 1 + helper(i+1, s[i], 1, remain_dels)
            
            # del
            del_curr_cost = float('inf')
            if remain_dels > 0:
                del_curr_cost = helper(i+1, curr_streak_char, streak_len, remain_dels-1)
            
            return min(keep_curr_cost, del_curr_cost)
    
        return helper(0, '', 0, k)