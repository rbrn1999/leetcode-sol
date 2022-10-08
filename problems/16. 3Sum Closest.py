# link: https://leetcode.com/problems/3sum-closest/
# solution reference: https://leetcode.com/problems/3sum-closest/discuss/8026

class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        ans = float('inf')
        nums.sort()
        # sort helps a lot in this type of problems cause we are not finding an exact match

        # freeze the first number then try the combinations of the other two with two-pointer stategy
        # Time Complexity: O(n), Space Complexity: O(1)
        for i in range(len(nums)):
            if i>0 and nums[i] == nums[i-1]:
                # skip duplicate (all combinations are included in the last iteration)
                continue

            low = i+1
            high = len(nums)-1

            while low < high:
                curSum = nums[i] + nums[low] + nums[high]

                if abs(target - curSum) < abs(target - ans):
                    ans = curSum

                if curSum < target:
                    low += 1
                elif curSum > target:
                    high -= 1
                else: # found an exact match
                    return curSum
        return ans
