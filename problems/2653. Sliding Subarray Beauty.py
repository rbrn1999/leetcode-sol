# link: https://leetcode.com/problems/sliding-subarray-beauty/

class Solution:
    def getSubarrayBeauty(self, nums: List[int], k: int, x: int) -> List[int]:
        answer = []
        bucket = [0]*50 # (-50 ~ -1)

        def findMinX():
            count = x
            for i in range(len(bucket)):
                count -= bucket[i]
                if count <= 0:
                    return i-50
            return 0


        for i in range(k):
            if nums[i] < 0:
                bucket[nums[i]+50] += 1

        answer.append(findMinX())

        for i in range(k, len(nums)):
            if nums[i-k] < 0:
                bucket[nums[i-k]+50] -= 1
            if nums[i] < 0:
                bucket[nums[i]+50] += 1

            answer.append(findMinX())

        return answer

