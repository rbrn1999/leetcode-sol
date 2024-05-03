# link: https://leetcode.com/problems/count-pairs-in-two-arrays/

class Solution:
    def countPairs(self, nums1: list[int], nums2: list[int]) -> int:
        # (nums1[i] - nums2[i]) + (nums1[j] - nums2[j]) > 0

        diffs = [nums1[i] - nums2[i] for i in range(len(nums1))]
        diffs.sort()
        answer = 0
        print(diffs)
        j = len(diffs) - 1
        for i in range(len(diffs)-1):
            while j > i and diffs[i] + diffs[j] > 0:
                j -= 1

            # j+1 is the smallest diff the statisfied, j+1 must be larger than i
            j = max(j, i)
            answer += len(diffs) - 1 - j

        return answer
