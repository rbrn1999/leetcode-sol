# link: https://leetcode.com/problems/find-all-anagrams-in-a-string/

class Solution:
    def findAnagrams(self, s: str, p: str) -> list[int]:
        result = []
        s_len, p_len = len(s), len(p)
        if s_len < p_len:
            return []
        p_count = [0] * 26
        s_count = [0] * 26
        for c in p:
            p_count[ord(c) - ord('a')] += 1
        for i in range(p_len):
            s_count[ord(s[i]) - ord('a')] += 1
        if p_count == s_count:
            result.append(0)
        for i in range(s_len-p_len):
            s_count[ord(s[i]) - ord('a')] -= 1
            s_count[ord(s[i+p_len]) - ord('a')] += 1
            if p_count == s_count:
                result.append(i+1)
        return result
