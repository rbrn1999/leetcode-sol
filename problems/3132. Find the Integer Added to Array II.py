# link: https://leetcode.com/problems/find-the-integer-added-to-array-ii/


class Solution:
    def minimumAddedInteger(self, nums1: list[int], nums2: list[int]) -> int:
        def check(nums1: list[int], nums2: list[int], diff: int) -> bool:
            skips = 0
            i = j = 0
            while i < len(nums1) and j < len(nums2):
                if nums1[i] + diff != nums2[j]:
                    skips += 1
                else:
                    j += 1

                if skips > 2:
                    return False
                i += 1

            return True


        answer = float('inf')
        nums1.sort()
        nums2.sort()

        for i in range(min(len(nums1), 3)):
            diff = nums2[0] - nums1[i]
            if diff < answer and check(nums1, nums2, diff):
                answer = diff

        return answer if type(answer) is int else -1
