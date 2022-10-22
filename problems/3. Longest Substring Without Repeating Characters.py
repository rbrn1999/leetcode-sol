# link: https://leetcode.com/problems/longest-substring-without-repeating-characters/

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        viewed = ""
        length = 0
        for c in s:
            if not c in viewed:
                viewed += c
            else:
                length = max(length, len(viewed))
                viewed = viewed[viewed.index(c)+1:] + c
        length = max(length, len(viewed))
        return length

    # using HashMap to fast search and record index
    # def lengthOfLongestSubstring(self, s: str) -> int:
    #     seenIndex = {}
    #     start = maxLength =  0
    #     for i, c in enumerate(s):
    #         if c not in seenIndex or seenIndex[c] < start: 
    #             seenIndex[c] = i
    #         else:
    #             maxLength = max(maxLength, i-start)
    #             start = seenIndex[c] + 1
    #             seenIndex[c] = i
    #             # the char index before i will not be erased,
    #             # so we have to double check at the if-statement above
                
    #     maxLength = max(maxLength, len(s)-start)
    #     return maxLength

    # using set
    # def lengthOfLongestSubstring(self, s: str) -> int:
    #    seen = set()
    #    maxLen = 0
    #    start = 0

    #    for i, c in enumerate(s):
    #        if c not in seen:
    #            seen.add(c)
    #        else:
    #            maxLen = max(maxLen, len(seen))
    #            start = s[start:i].index(c) + start + 1
    #            seen = set(s[start:i+1])
    #    maxLen = max(maxLen, len(s)-start)
    #    return maxLen
