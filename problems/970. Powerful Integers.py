# link: https://leetcode.com/problems/powerful-integers/

class Solution:
    def powerfulIntegers(self, x: int, y: int, bound: int) -> List[int]:
        result = set()
        seen = set()

        def dfs(num1, num2):
            if num1 + num2 > bound or (num1, num2) in seen:
                return
            else:
                seen.add((num1, num2))
                result.add(num1 + num2)

            dfs(num1 * x, num2)
            dfs(num1, num2 * y)

        dfs(1, 1)
        return list(result)

