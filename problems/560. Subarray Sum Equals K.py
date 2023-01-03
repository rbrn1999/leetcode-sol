# link: https://leetcode.com/problems/subarray-sum-equals-k/

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        n = len(nums)
        total = 0
        prefixSum = [0] #avoid out of bound
        for i in range(n):
            total += nums[i]
            prefixSum.append(total)

        count = 0
        seenCount = {}
        for i in range(n+1):
            if prefixSum[i] - k in seenCount:
                count += seenCount[prefixSum[i]-k]

            seenCount[prefixSum[i]] = seenCount.get(prefixSum[i], 0) + 1

        return count

