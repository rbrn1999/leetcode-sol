# link: https://leetcode.com/problems/next-greater-element-iii/

class Solution:
    def nextGreaterElement(self, n: int) -> int:        
        digits = [int(c) for c in str(n)]

        # find next permutation
        # find first decreasing from right to left
        pivot = len(digits) - 2
        while pivot >= 0 and digits[pivot] >= digits[pivot+1]:
            pivot -= 1
        
        if pivot == -1:
            return -1

        # find smallest number that's larger than digits[pivot]
        low = pivot + 1 
        high = len(digits) - 1

        while low < high:
            mid = (low + high + 1) // 2
            if digits[mid] > digits[pivot]:
                low = mid
            else:
                high = mid - 1
        
        digits[pivot], digits[low] = digits[low], digits[pivot]

        # digits[pivot+1:] is descending, reverse to make it in ascending order
        l = pivot + 1
        r = len(digits) - 1
        while l < r:
            digits[l], digits[r] = digits[r], digits[l]
            l += 1
            r -= 1
        
        val = int(''.join(str(d) for d in digits))
        return val if val < 2 ** 31 else -1