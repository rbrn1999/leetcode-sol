# link: https://leetcode.com/problems/longest-repeating-character-replacement/
# solution reference: https://www.youtube.com/watch?v=gqXU1UyA8pk

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        charCount = {}
        maxFreq = 1
        maxLen = 0
        for r in range(len(s)):
            charCount[s[r]] = charCount.get(s[r], 0) + 1
            # maxLen will only get larger when there's a greater maxFreq (canidate length <= maxFreq + k, hence no way it'll be larger)
            # so there's no need to update when moving l (shrinking the window)
            # by only updating when the freqence increases, the time complexity goes from O(n * 26) to O(n) (no need to scan the whole dict)
            maxFreq = max(maxFreq, charCount[s[r]]) 
            while (r-l+1)-maxFreq > k:
                charCount[s[l]] -= 1
                l += 1
            maxLen = max(maxLen, r-l+1)
        
        return maxLen