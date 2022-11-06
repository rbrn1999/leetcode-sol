# link: https://leetcode.com/problems/longest-palindrome-by-concatenating-two-letter-words/

class Solution:
    def longestPalindrome(self, words: List[str]) -> int:
        pairCandidate = {}
        pairCount = 0

        for word in words:
            if pairCandidate.get(word, 0) > 0:
                pairCandidate[word] -= 1
                if pairCandidate[word] == 0:
                    del pairCandidate[word]
                pairCount += 1
            else:
                pairCandidate[word[::-1]] = pairCandidate.get(word[::-1], 0) + 1

        hasMidWord = False
        for word in pairCandidate:
            if word[0] == word[1]:
                hasMidWord = True

        return 2 * 2 * pairCount + 2 * (int(hasMidWord))
