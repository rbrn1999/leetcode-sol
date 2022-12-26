# link: https://leetcode.com/problems/find-k-th-smallest-pair-distance/description/
# solution: https://leetcode.com/problems/find-k-th-smallest-pair-distance/solutions/127408/official-solution/


class Solution:
    def smallestDistancePair(self, nums: list[int], k: int) -> int:
        def isPossible(guess):
            # sliding window: check if count of pair "distances less or equal to guess" >= k
            left = 0
            count = 0
            for right in range(len(nums)):
                while nums[right] - nums[left] > guess:
                    left += 1        
                count += right - left
                
            return count >= k
        
        nums.sort()
        # low, high presents the possible answers' bound
        low = 0
        high = nums[-1] - nums[0]
        
        while low < high:
            mid = (low + high) // 2
            if isPossible(mid): 
                # pairs with distance less or equal to mid is more than or equal to k
                # make the upper bound tighter
                high = mid
            else:
                # pairs with distance less or equal to mid less than k
                # make the lower bound higher to search the upper half of possible answers
                low = mid + 1
        
        return low