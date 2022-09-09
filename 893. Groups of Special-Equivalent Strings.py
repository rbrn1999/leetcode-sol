# link: https://leetcode.com/problems/groups-of-special-equivalent-strings/

class EncodeString:
    def __init__(self, string):
        self.odd = [0] * 26
        self.even = [0] * 26
        for c in string[1::2]:
            self.odd[ord(c) - ord('a')] += 1
        for c in string[::2]:
            self.even[ord(c) - ord('a')] += 1

    def __hash__(self):
        return hash(str(self.even + self.odd))

    def __eq__(self, other):
        return self.odd == other.odd and self.even == other.even



class Solution:
    def numSpecialEquivGroups(self, words: List[str]) -> int:
        s = set(EncodeString(word) for word in words)
        return len(s)


