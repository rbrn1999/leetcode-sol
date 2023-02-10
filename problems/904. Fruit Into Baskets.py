# link: https://leetcode.com/problems/fruit-into-baskets/

class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        max_count = 0
        choosen_fruits = set()
        start = 0
        next_start = 0

        for i in range(len(fruits)):
            if len(choosen_fruits) < 2:
                choosen_fruits.add(fruits[i])
            elif fruits[i] not in choosen_fruits:
                max_count = max(max_count, i - start)
                choosen_fruits = set(fruits[i-1:i+1])
                start = next_start

            if len(choosen_fruits) > 0 and fruits[i] != fruits[i-1]:
                next_start = i

        max_count = max(max_count, len(fruits) - start)
        return max_count

