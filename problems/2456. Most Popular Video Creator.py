# link: https://leetcode.com/problems/most-popular-video-creator/

from collections import defaultdict
class Solution:
    def mostPopularCreator(self, creators: list[str], ids: list[str], views: list[int]) -> list[list[str]]:
        n = len(creators)
        maxCount = -1
        creator_inds = defaultdict(lambda :[[], 0] )
        for i in range(n):
            creator_inds[creators[i]][0].append(i)
            creator_inds[creators[i]][1] += views[i]
            maxCount = max(maxCount, creator_inds[creators[i]][1])
        
        res = []
        for name, val in creator_inds.items():
            if val[1] != maxCount:
                continue
            max_ind = min(val[0], key=lambda i: (-views[i], ids[i])) # max view with smallest id
            res.append([name, ids[max_ind]])
        
        return res