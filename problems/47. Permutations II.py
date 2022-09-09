# link: https://leetcode.com/problems/permutations-ii/

from collections import Counter
class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        results = []
        def backtrack(comb, counter):
            if len(comb) == len(nums):
                results.append(comb)
                return 
            
            for num in counter:
                if counter[num] > 0:
                    counter[num] -= 1
                    backtrack(comb + [num], counter)
                    counter[num] += 1
                    
        backtrack([], Counter(nums))  
        return results