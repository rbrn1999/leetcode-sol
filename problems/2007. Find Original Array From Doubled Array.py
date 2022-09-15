# link: https://leetcode.com/problems/find-original-array-from-doubled-array/

class Solution:
    def findOriginalArray(self, changed: List[int]) -> List[int]:
        visitCount = {}
        result = []
        for val in sorted(changed):
            if val % 2 == 0 and val//2 in visitCount:
                visitCount[val//2] -= 1
                if visitCount[val//2] == 0:
                    del visitCount[val//2]
                result.append(val // 2)
            else:
                visitCount.setdefault(val, 0)
                visitCount[val] += 1
        if len(visitCount) != 0:
            result = []
        return result
