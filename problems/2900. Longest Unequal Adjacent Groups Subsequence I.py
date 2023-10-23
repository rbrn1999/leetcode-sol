# link: https://leetcode.com/problems/longest-unequal-adjacent-groups-subsequence-i/

class Solution:
    def getWordsInLongestSubsequence(self, n: int, words: list[str], groups: list[int]) -> list[str]:
        answer = []
        prev = -1
        for i in range(len(words)):
            if groups[i] != prev:
                answer.append(words[i])
                prev = groups[i]
            elif len(words[i]) > len(answer[-1]):
                answer[-1] = words[i]
        
        return answer
                