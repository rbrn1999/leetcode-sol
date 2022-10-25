# link: https://leetcode.com/problems/minimum-window-substring/
# soulution reference: https://leetcode.com/problems/minimum-window-substring/discuss/226911/

from collections import Counter
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        targetCharCount = Counter(t)
        start = 0
        min_window = ""
        notInWindowCharCount = len(t)
        
        for end in range(1, len(s)+1): # [start~end)
            if targetCharCount[s[end-1]] > 0:
                notInWindowCharCount -= 1
            if s[end-1] in targetCharCount:
                targetCharCount[s[end-1]] -= 1
            
            # all target characters appears in [start~end)
            # move start to shrink the window to find mininum length canidate
            while notInWindowCharCount == 0:
                window_len = end - start
                if not min_window or window_len < len(min_window):
                    min_window = s[start:end]
                
                if s[start] in targetCharCount:
                    targetCharCount[s[start]] += 1
                if targetCharCount[s[start]] > 0:
                    notInWindowCharCount += 1
                    
                start += 1
        
        return min_window

# Solution w/o using Counter
# class Solution:
#     def minWindow(self, s: str, t: str) -> str:
#         targetCharCount = {}
#         for c in t:
#             targetCharCount[c] = targetCharCount.get(c, 0) + 1

#         start = 0
#         min_window = ""
#         notInWindowCharCount = len(t)
        
#         for end in range(1, len(s)+1): # [start~end)
#             if targetCharCount.get(s[end-1], 0) > 0:
#                 notInWindowCharCount -= 1
#             if s[end-1] in targetCharCount:
#                 targetCharCount[s[end-1]] -= 1
            
#             # all target characters appears in [start~end)
#             # move start to shrink the window to find mininum length canidate
#             while notInWindowCharCount == 0:
#                 window_len = end - start
#                 if not min_window or window_len < len(min_window):
#                     min_window = s[start:end]
                
#                 if s[start] in targetCharCount:
#                     targetCharCount[s[start]] += 1
#                 if targetCharCount.get(s[start], 0) > 0:
#                     notInWindowCharCount += 1
                    
#                 start += 1
        
#         return min_window