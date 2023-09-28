# link: https://leetcode.com/problems/merge-triplets-to-form-target-triplet/

class Solution:
    def mergeTriplets(self, triplets: list[list[int]], target: list[int]) -> bool:
        for i in range(3):
            flag = False
            for t in triplets:
                if target[i] == t[i] and all(t[j] <= target[j] for j in range(3)):
                    flag = True
                    break
            if not flag:
                return False
        
        return True