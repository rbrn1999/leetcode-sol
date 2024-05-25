# link: https://leetcode.com/problems/longest-repeating-substring/

# sliding window
class Solution:
    def longestRepeatingSubstring(self, s: str) -> int:
        def hasRepeat(size: int) -> bool:
            seen = set()
            for i in range(len(s)-size+1):
                substring = s[i:i+size]
                if hash(substring) in seen:
                    return True
                else:
                    seen.add(hash(substring))
            
            return False

        for size in range(len(s)-1, 0, -1):
            if hasRepeat(size):
                return size
        
        return 0

# binary search
class Solution:
    def longestRepeatingSubstring(self, s: str) -> int:
        def hasRepeat(size: int) -> bool:
            seen = set()
            for i in range(len(s)-size+1):
                substring = s[i:i+size]
                if hash(substring) in seen:
                    return True
                else:
                    seen.add(hash(substring))
            
            return False

        low = 0
        high = len(s) - 1

        while low < high:
            mid = (low + high + 1) // 2
            if hasRepeat(mid):
                low = mid
            else:
                high = mid - 1

        return low