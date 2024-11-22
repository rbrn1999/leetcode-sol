# link: https://leetcode.com/problems/minimized-maximum-of-products-distributed-to-any-store/

import math
class Solution:
    def minimizedMaximum(self, n: int, quantities: list[int]) -> int:
        def canDistribute(max_product_count: int, store_count: int) -> bool:
            for q in quantities:
                count = math.ceil(q / max_product_count)
                if count > store_count:
                    return False
                else:
                    store_count -= count

            return True

        low = 1
        high = max(quantities)
        while low < high:
            mid = (low + high) // 2
            if canDistribute(mid, n):
                high = mid
            else:
                low = mid + 1

        return low
