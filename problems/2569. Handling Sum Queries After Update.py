# link: https://leetcode.com/problems/handling-sum-queries-after-update/

class Solution:
    def handleQuery(self, nums1: List[int], nums2: List[int], queries: List[List[int]]) -> List[int]:
        results = []
        sum2 = sum(nums2)
        n = len(nums1)
        nums1 = int(''.join([str(num) for num in nums1]), 2)


        for q in queries:
            if q[0] == 1:
                # mask_s = '1' * (q[2]-q[1]+1) + '0' * (n-q[2]-1)
                # mask = int(mask_s, 2)
                mask = 2 ** (n-q[1]) - 2 ** (n-q[2]-1)
                nums1 = nums1 ^ mask
            elif q[0] == 2:
                sum2 += nums1.bit_count() * q[1]
            elif q[0] == 3:
                results.append(sum2)
            else:
                pass

        return results
