# link: https://leetcode.com/problems/non-decreasing-subsequences/

import copy
class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        # dict: key: last value in sequence, value: set[tuple[int]]
        subSequences = {}
        for i in range(len(nums)):
            isFirstApearance = False
            if nums[i] not in subSequences:
                isFirstApearance = True
                subSequences[nums[i]] = set()
            temp_subSequence = copy.deepcopy(subSequences)
            for prevNum in temp_subSequence:
                if prevNum > nums[i] or (isFirstApearance and prevNum == nums[i]):
                    continue
                for subSeq in temp_subSequence[prevNum]:
                    newSeq = subSeq + (nums[i],)
                    subSequences[nums[i]].add(newSeq)

                subSequences[nums[i]].add((prevNum, nums[i]))

        result = []
        for subSeqs in subSequences.values():
            for seq in subSeqs:
                result.append(list(seq))

        return result
