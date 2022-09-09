# link: https://leetcode.com/problems/merge-sorted-array/

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        ptr = 0
        for num2 in nums2:
            del nums1[-1]
            while ptr < m and nums1[ptr] < num2:
                ptr += 1

            # print('inserting ' + str(num2) + ' at ' + str(ptr) + ', m= ' + str(m))
            nums1.insert(ptr, num2)
            # print(nums1)
            m += 1

    # using binary search
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        del nums1[m:]
        for i, num in enumerate(nums2):
            ind = bisect_left(nums1, num, 0, m+i)
            nums1.insert(ind, num)


