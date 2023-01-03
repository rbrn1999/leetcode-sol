# link: https://leetcode.com/problems/number-of-sub-arrays-of-size-k-and-average-greater-than-or-equal-to-threshold/

class Solution:
    # initialize the window in loop
    def numOfSubarrays(self, arr: list[int], k: int, threshold: int) -> int:
        cur_sum, count = 0, 0
        l = 0
        for r in range(len(arr)):
            cur_sum += arr[r]
            if r - l + 1 < k:
                continue
            if r - l + 1 > k:
                cur_sum -= arr[l]
                l += 1
            # r - l == k
            if cur_sum / k >= threshold:
                count += 1
        
        return count
    # initialize the window first
    def numOfSubarrays(self, arr: list[int], k: int, threshold: int) -> int:
        avg, count = 0, 0
        for i in range(k):
            avg += arr[i] / k
        if avg >= threshold:
            count += 1

        for l in range(1, len(arr) - (k-1)):
            avg = avg - arr[l-1]/k + arr[l+k-1] / k
            count += 1 if avg >= threshold else 0

        return count

