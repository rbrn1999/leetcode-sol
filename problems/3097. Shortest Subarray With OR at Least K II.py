# link: https://leetcode.com/problems/shortest-subarray-with-or-at-least-k-ii/

class Solution:
    def minimumSubarrayLength(self, nums: list[int], k: int) -> int:
        bits = [0] * 32
        length = len(nums) + 1
        cur = 0
        l = 0
        for r in range(len(nums)):
            num = nums[r]
            e = 0
            cur |= num
            while num > 0:
                bits[e] += num % 2
                num >>= 1
                e += 1

            while l <= r and cur >= k:
                length = min(length, r-l+1)
                num = nums[l]
                e = 0
                while num > 0:
                    if num % 2 == 1:
                        bits[e] -= 1
                        if bits[e] == 0:
                            cur -= 1 << e
                    num >>= 1
                    e += 1
                l += 1

        return length if length <= len(nums) else -1
