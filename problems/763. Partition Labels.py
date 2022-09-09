# link: https://leetcode.com/problems/partition-labels/
class Solution:
    def partitionLabels(self, s: str): #-> List[int]:
        
        def singleLabel(start):
            end = s.rindex(s[start])
            
            for index in range(end+1, len(s)):
                if s[index] in s[start:end+1]:
                    end = index

            return end
        
        partitions = []
        tempStart = 0
        
        while tempStart < len(s):
            tempEnd = singleLabel(tempStart)
            partitions.append(tempEnd - tempStart + 1)
            print(f'start: {tempStart}, end: {tempEnd}')
            print(s[tempStart:tempEnd+1])
            tempStart = tempEnd+1
        return partitions

sol = Solution()
print(sol.partitionLabels("qiejxqfnqceocmy"))
