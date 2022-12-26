# link: https://leetcode.com/problems/median-of-two-sorted-arrays/

# solution: https://leetcode.com/problems/median-of-two-sorted-arrays/solutions/2496/

class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        m, n = len(nums1), len(nums2)
        def getKth(ind1, ind2, k):
            if ind1 >= m:
                return nums2[ind2+k-1]
            if ind2 >= n:
                return nums1[ind1+k-1]
            if k == 1:
                return min(nums1[ind1], nums2[ind2])
            
            mid1, mid2 = ind1 + k//2 - 1, ind2 + k//2 - 1
            val1 = nums1[mid1] if mid1 < m else float('inf')
            val2 = nums2[mid2] if mid2 < n else float('inf')
            
            if val1 < val2:
                return getKth(mid1 + 1, ind2, k - k//2)
            else:
                return getKth(ind1, mid2 + 1, k - k//2)
        
        
        if (m + n) % 2:
            return getKth(0, 0, (m + n) // 2 + 1)
        else:
            return (getKth(0, 0, (m + n) // 2) + getKth(0, 0, (m + n) // 2 + 1)) / 2