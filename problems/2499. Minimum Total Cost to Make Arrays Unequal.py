# link: https://leetcode.com/problems/minimum-total-cost-to-make-arrays-unequal/

class Solution:
    def minimumTotalCost(self, nums1: List[int], nums2: List[int]) -> int:
        n = len(nums1)
        replace_inds = [i for i in range(n) if nums1[i] == nums2[i]]
        valid_inds = [i for i in range(n) if nums1[i] != nums2[i]]
        dups = {}
        maxDup = 0
        for i in replace_inds:
            dups.setdefault(nums1[i], 0)
            dups[nums1[i]] += 1
            if maxDup not in dups or dups[nums1[i]] > dups[maxDup]:
                maxDup = nums1[i]

        if not dups:
            return 0

        conpensateCount = max(0, 2*dups[maxDup] - sum(dups.values()))

        cost = sum(replace_inds)
        i = 0
        valid_len = len(valid_inds)

        while conpensateCount > 0:
            if i == valid_len:
                return -1
            if nums1[valid_inds[i]] != maxDup and nums2[valid_inds[i]] != maxDup:
                cost += valid_inds[i]
                conpensateCount -= 1

            i += 1

        return cost

