# link: https://leetcode.com/problems/number-of-laser-beams-in-a-bank/

class Solution:
    def numberOfBeams(self, bank: list[str]) -> int:
        prev_count = 0
        total_count = 0
        for row in bank:
            count = row.count('1')
            if count > 0:
                total_count += prev_count * count
                prev_count = count
        
        return total_count