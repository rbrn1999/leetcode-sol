# link: https://leetcode.com/problems/binary-trees-with-factors/

from functools import cache
class Solution:
    def numFactoredBinaryTrees(self, arr: list[int]) -> int:
        nums = set(arr)
        @cache
        def helper(root: int) -> int:
            count = 1
            for num_1 in nums:
                num_2 = root // num_1
                if root == num_1 * num_2 and num_2 in nums:
                    count += helper(num_1) * helper(num_2)
                    count %= (10 ** 9 + 7)
            
            return count
        
        ans = 0
        for num in arr:
            ans += helper(num)
            ans %= (10 ** 9 + 7)
        
        return ans