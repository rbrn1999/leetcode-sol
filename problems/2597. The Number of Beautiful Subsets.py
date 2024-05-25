# link: https://leetcode.com/problems/the-number-of-beautiful-subsets/

class Solution:
    def beautifulSubsets(self, nums: list[int], k: int) -> int:
        nums.sort()
        def dfs(i: int, freq: dict) -> int:
            if i == len(nums):
                if not freq:
                    return 0
                else:
                    return 1
            
            count = dfs(i+1, freq)
            if nums[i] - k not in freq:
                freq[nums[i]] = freq.get(nums[i], 0) + 1
                count += dfs(i+1, freq)
                freq[nums[i]] -= 1
                if freq[nums[i]] == 0:
                    del freq[nums[i]]
            
            return count
        
        return dfs(0, {})