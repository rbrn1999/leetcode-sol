# link: https://leetcode.com/problems/compare-version-numbers/

class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        l1, l2 = 0, 0
        while l1 < len(version1) and l2 < len(version2):
            r1 = l1 + 1
            r2 = l2 + 1
            while r1 < len(version1):
                if version1[r1] != '.':
                    r1 += 1
                else:
                    break
            while r2 < len(version2):
                if version2[r2] != '.':
                    r2 += 1
                else:
                    break

            num1 = int(version1[l1:r1])
            num2 = int(version2[l2:r2])
            if num1 < num2:
                return -1
            if num1 > num2:
                return 1
            l1 = r1 + 1
            l2 = r2 + 1

        while l1 < len(version1):
            r1 = l1 + 1
            while r1 < len(version1):
                if version1[r1] != '.':
                    r1 += 1
                else:
                    break
            if int(version1[l1:r1]) > 0:
                return 1
            l1 = r1+1

        while l2 < len(version2):
            r2 = l2 + 1
            while r2 < len(version2):
                if version2[r2] != '.':
                    r2 += 1
                else:
                    break
            if int(version2[l2:r2]) > 0:
                return -1
            l2 = r2+1

        return 0
