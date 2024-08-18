# link: https://leetcode.com/problems/lemonade-change/

class Solution:
    def lemonadeChange(self, bills: list[int]) -> bool:
        changes = [0, 0]
        value = [5, 10]

        for bill in bills:
            change = bill - 5
            for i in range(1, -1, -1):
                amount = min(changes[i], change//value[i])
                changes[i] -= amount
                change -= value[i] * amount
            
            if change > 0:
                return False

            if bill == 5:
                changes[0] += 1
            if bill == 10:
                changes[1] += 1
            
        return True