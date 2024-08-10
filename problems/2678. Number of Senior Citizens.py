# link: https://leetcode.com/problems/number-of-senior-citizens/

class Solution:
    def countSeniors(self, details: list[str]) -> int:
        count = 0
        for detail in details:
            if int(detail[11:13]) > 60:
                count += 1

        return count
