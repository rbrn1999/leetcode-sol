# link: https://leetcode.com/problems/substring-with-concatenation-of-all-words/

class Solution:                    
    def findSubstring(self, s: str, words: list[str]) -> list[int]:
        def substract(d, key):
            if key in d:
                d[key] -= 1
            else:
                return
            if d[key] == 0:
                del d[key]

        wordDict = dict()
        for word in words:
            wordDict.setdefault(word, 0)
            wordDict[word] += 1
        
        k = len(words[0])
        n = len(words)
        
        def slidingWindow(ind):
            wordDict_copy = wordDict.copy()
            left = ind
            right = ind + k
            result = []
            
            while right <= len(s):
                word = s[right-k:right]
                if word in wordDict_copy:
                    substract(wordDict_copy, word)
                elif word in wordDict:
                    wordDict_copy = wordDict.copy()
                    left = right-k
                    # backtrack to include all valid words just before 'left'
                    while s[left:left+k] in wordDict_copy:
                        substract(wordDict_copy, s[left:left+k])
                        left -= k
                    # add the extra -= k when exiting the loop back
                    left += k
                else:
                    wordDict_copy = wordDict.copy()
                    left = right

                if len(wordDict_copy) == 0:
                    result.append(left)

                # check window length and remove word
                if right - left == n*k:
                    if len(wordDict_copy):
                        word = s[left:left+k]
                        substract(wordDict_copy, word)
                    left += k

                right += k
            
            return result
        
        result = []
        for i in range(k):
            result += slidingWindow(i)
        return result

print(Solution().findSubstring("bcabbcaabbccacacbabccacaababcbb", \
                            ["c","b","a","c","a","a","a","b","c"]
                            ))