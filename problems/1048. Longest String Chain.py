# link: https://leetcode.com/problems/longest-string-chain/

class Solution:
    def longestStrChain(self, words: list[str]) -> int:
        chain_length = {} # last_str: length
        words.sort(key=len)
        for word in words:
            l = 1
            for i in range(len(word)):
                prev = word[:i] + word[i+1:]
                if prev in chain_length:
                    l = max(l, chain_length[prev]+1)

            chain_length[word] = l

        return max(chain_length.values())