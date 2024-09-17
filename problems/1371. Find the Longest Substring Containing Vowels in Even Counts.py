# link: https://leetcode.com/problems/find-the-longest-substring-containing-vowels-in-even-counts/

class Solution:
    def findTheLongestSubstring(self, s: str) -> int:
        vowels = {'a': 0, 'e': 1, 'i': 2, 'o': 3, 'u': 4}
        state_index = {0: -1}
        state = 0
        result = 0
        for i in range(len(s)):
            if s[i] in vowels:
                state ^= 1 << vowels[s[i]]

            if state not in state_index:
                state_index[state] = i
            else:
                result = max(result, i - state_index[state])

        return result
