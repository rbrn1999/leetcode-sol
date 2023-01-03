# link: https://leetcode.com/problems/range-sum-query-immutable/

class NumArray:

    def __init__(self, nums: List[int]):
        self.prefixSum = [nums[0]]
        for i in range(1, len(nums)):
            self.prefixSum.append(self.prefixSum[i-1] + nums[i])

    def sumRange(self, left: int, right: int) -> int:
        return self.prefixSum[right] - (self.prefixSum[left-1] if left-1 >= 0 else 0)


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)
