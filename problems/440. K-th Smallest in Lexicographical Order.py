# link: https://leetcode.com/problems/k-th-smallest-in-lexicographical-order/

class Solution:
    def findKthNumber(self, n: int, k: int) -> int:
        def count(cur: int) -> int: # count subtree size with prefix cur
            res = 0
            neighbor = cur + 1
            while cur <= n: # count nodes level-by-level
                res += min(neighbor, n+1) - cur
                cur *= 10
                neighbor *= 10

            return res

        cur = 1
        i = 1

        while i < k:
            steps = count(cur)
            if i + steps <= k:
                cur = cur + 1
                i += steps
            else:
                cur *= 10
                i += 1

        return cur
