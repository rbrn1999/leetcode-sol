# link: https://leetcode.com/problems/partition-labels/
class Solution:
    def partitionLabels(self, s: str): #-> List[int]:
        last_occr = {}
        for i, c in enumerate(s):
            last_occr[c] = i
        
        partitions = []
        l = r = 0
        for i, c in enumerate(s):
            r = max(r, last_occr[c])
            if i == r:
                partitions.append(r-l+1)
                l = r = i + 1
        
        return partitions
