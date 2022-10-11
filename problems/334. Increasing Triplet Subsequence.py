# link: https://leetcode.com/problems/increasing-triplet-subsequence/
# solution reference: https://leetcode.com/problems/increasing-triplet-subsequence/discuss/78993

class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        low = mid = float('inf')

        for num in nums:
            #include equal to stop num going into the statements below

            # update the lowest value
            if num <= low:
                low = num
            elif num <= mid: # update mid if low < num <= mid
                mid = num
            else:
                return True
                # low, mid, num may not be the sequence
                # but we don't need to find it anyway

        return False
