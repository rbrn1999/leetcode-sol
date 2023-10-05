# link: https://leetcode.com/problems/majority-element-ii/

class Solution:
    def majorityElement(self, nums: list[int]) -> list[int]:
        count = {} # only keep the two most frequent numbers
        for num in nums:
            count[num] = count.get(num, 0) + 1
            if len(count) == 3:
                for num in list(count.keys()):
                    count[num] -= 1
                    if count[num] == 0:
                        del count[num]
        
        for num in count:
            count[num] = 0
        
        for num in nums:
            if num not in count:
                continue
            count[num] += 1
        
        return [num for num in count if count[num] > len(nums) // 3]