# link: https://leetcode.com/problems/ransom-note/

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        rCount = [0]*26
        mCount = [0]*26

        for c in ransomNote:
            rCount[ord(c)-ord('a')] += 1

        for c in magazine:
            mCount[ord(c)-ord('a')] += 1

        return all([ mCount[i]-rCount[i] >= 0 for i in range(26)])
