# link: https://leetcode.com/problems/check-if-the-sentence-is-pangram/

class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        s = set(range(26))
        for c in sentence:
            if ord(c)-ord('a') in s:
                s.remove(ord(c)-ord('a'))
                if len(s) == 0:
                    return True
        return False

    # one liner
    # return len(set([c for c in sentence])) == 26
