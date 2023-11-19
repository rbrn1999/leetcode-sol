# link: https://leetcode.com/problems/unique-length-3-palindromic-subsequences/

class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        ans = 0
        for start in set(s):
            unique_characters = set()
            inSequence = False
            count = 0
            for c in s:
                if c == start:
                    if not inSequence:
                        inSequence = True
                    else:
                        count = len(unique_characters)
                        # account the 3rd character as a future 2nd character
                        unique_characters.add(c) 
                elif inSequence:
                   unique_characters.add(c)

            ans += count

        return ans 
                