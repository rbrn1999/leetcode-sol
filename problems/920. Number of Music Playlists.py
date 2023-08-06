# link: https://leetcode.com/problems/number-of-music-playlists/

from functools import cache
class Solution:
    def numMusicPlaylists(self, n: int, goal: int, k: int) -> int:
        #parm (i: playlist length, j: unique songs)
        @cache
        def helper(i: int, j: int) -> int:
            # return the combinations if song from (i~n)
            if i == goal:
                return int(j == n)
            count = 0
            if j < n: # choose new unique song
                count += (n-j) * helper(i+1, j+1)
            if j > k: # choose song played # when j <= k, songs played = j
                count += (j-k) * helper(i+1, j)
            
            return count % (10 ** 9 + 7)
        
        return helper(0, 0)
