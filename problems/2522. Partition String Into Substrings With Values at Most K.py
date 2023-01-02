# link: https://leetcode.com/problems/partition-string-into-substrings-with-values-at-most-k/

class Solution:
    def minimumPartition(self, s: str, k: int) -> int:
        if k < 9:
            for c in s:
                if int(c) <= k:
                    continue
                return -1

        n = len(s)
        def isValid(partitions):
            i = 0
            while i < n:
                j = i
                while j < n and int(s[i:j+1]) <= k:
                    j += 1
                partitions -= 1
                i = j
            return partitions >= 0

        low = 1
        high = n
        result = -1
        while low <= high:
            mid = low + (high - low) // 2
            if isValid(mid):
                result = mid
                high = mid - 1
            else:
                low = mid + 1

        return result

