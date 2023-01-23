# link: https://leetcode.com/problems/non-decreasing-subsequences/
class Solution:
    def findSubsequences(self, nums: list[int]) -> list[list[int]]:
        seqs = set()
        for i in range(len(nums)):
            cur_seqs = set()
            for seq in seqs:
                if nums[i] >= seq[-1]:
                    cur_seqs.add(seq + (nums[i],))
            seqs = seqs.union(cur_seqs)
            for j in range(i):
                if nums[i] >= nums[j]:
                    seqs.add((nums[j], nums[i]))
        return [list(seq) for seq in seqs]
