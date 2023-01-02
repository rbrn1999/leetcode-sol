# link: https://leetcode.com/problems/jump-game-ii/
# solution reference: https://youtu.be/dJ7sWiOoK7g

'''
Greedy, BFS
Time Complexity:    O(n)
Space Complexity:   O(1)
'''

class Solution:
    def jump(self, nums: list[int]) -> int:
        n = len(nums)
        start = end = steps = 0

        while end < n - 1:
            new_end = 0
            for i in range(start, end+1):
                new_end = max(new_end, min(i+nums[i], n-1))
            
            steps += 1
            start, end = end + 1, new_end
        
        return steps