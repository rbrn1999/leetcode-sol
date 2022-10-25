# link: https://leetcode.com/problems/group-anagrams/

from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        wordGroup = defaultdict(list)
        for s in strs:
            charCount = [0]*26
            for c in s:
                charCount[ord(c)-ord('a')] += 1
            wordGroup[tuple(charCount)].append(s)
        return list(wordGroup.values())
