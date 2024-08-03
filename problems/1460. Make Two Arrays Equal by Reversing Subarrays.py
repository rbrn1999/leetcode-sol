# link: https://leetcode.com/problems/make-two-arrays-equal-by-reversing-subarrays/

class Solution:
    def canBeEqual(self, target: list[int], arr: list[int]) -> bool:
        count = {}
        for t in target:
            count[t] = count.get(t, 0) + 1
        
        for num in arr:
            if num not in count:
                return False
            else:
                count[num] -= 1
                if count[num] == 0:
                    del count[num]
        
        return True