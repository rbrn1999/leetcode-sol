# link: https://leetcode.com/problems/append-characters-to-string-to-make-subsequence/

class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        t_ind = 0
        t_len = len(t)
        for c in s:
            if c == t[t_ind]:
                t_ind += 1
                if t_ind == len(t):
                    break

        return t_len - t_ind

