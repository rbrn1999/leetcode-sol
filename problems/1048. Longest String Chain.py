# link: https://leetcode.com/problems/longest-string-chain/

from collections import defaultdict
class Solution:
    def longestStrChain(self, words: list[str]) -> int:
        def match(pre, cur) -> bool:
            if len(cur) - len(pre) != 1:
                return False
            skip = i = 0
            while i < len(pre):
                if pre[i] != cur[i+skip]:
                    skip += 1
                else:
                    i += 1
                if skip > 1:
                    return False
            return True
        
        lengthDict = defaultdict(list)
        for word in words:
            lengthDict[len(word)].append(word)
        
        # commented code is for tracing the path
        @cache
        def dfs(word):
            count = 0
            # path = []
            for pre in lengthDict[len(word)-1]:
                if match(pre, word):
                    count = max(count, dfs(pre))
                    # tCount, tPath = dfs(pre)
                    # if tCount > count:
                    #     count, path = tCount, tPath + [word]
            return count+1  #, path
        
        n = max(lengthDict.keys())
        ans = 0
        # dp = []
        for l in range(1, n+1):
            for word in lengthDict[l]:
                ans = max(ans, dfs(word))
                # dp.append(dfs(word))
                
        return ans # max(dp)[0]
        

