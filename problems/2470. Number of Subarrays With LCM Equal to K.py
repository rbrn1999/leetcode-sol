# link: https://leetcode.com/problems/number-of-subarrays-with-lcm-equal-to-k/

class Solution:
    def subarrayLCM(self, nums: List[int], k: int) -> int:
        memo = {}
        count = 0
        for i in range(len(nums)):
            curLcm = nums[i]
            for j in range(i, len(nums)):
                if (curLcm, nums[j]) not in memo:
                    curLcm = math.lcm(curLcm, nums[j])
                    memo[(curLcm, nums[j])] = curLcm
                    memo[(nums[j]), curLcm] = curLcm
                else:
                    curLcm = memo[(curLcm, nums[j])]
                if curLcm == k:
                    count += 1
                elif curLcm > k:
                    break
        return count

