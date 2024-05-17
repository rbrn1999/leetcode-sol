# link: https://leetcode.com/problems/longest-uncommon-subsequence-ii/

class Solution:
    def findLUSlength(self, strs: List[str]) -> int:
        def isSubsequence(s1: str, s2: str) -> bool:
            i = 0
            for c in word:
                if c != s[i]:
                    continue
                i += 1
                if i == len(s):
                    return False

            return True

        strs.sort(key=lambda s: [len(s), s])
        longer_words = []

        while strs:
            s = strs.pop()
            valid = True
            while strs and strs[-1] == s:
                valid = False
                strs.pop()

            if not valid:
                longer_words.append(s)
                continue

            for word in longer_words:
                if not isSubsequence(s, word):
                    valid = False

            if valid:
                return len(s)

            longer_words.append(s)


        return -1
