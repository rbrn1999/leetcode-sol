# link: https://leetcode.com/problems/lexicographical-numbers/

# Recursion
class Solution:
    def lexicalOrder(self, n: int) -> list[int]:
        stack = [1]
        result = []
        def dfs() -> None:
            if not stack:
                return

            num = int(''.join(str(digit) for digit in stack))
            if num > n:
                return

            result.append(num)
            stack.append(0)
            dfs()
            stack.pop()

            if stack[-1] < 9:
                stack[-1] += 1
                dfs()

        dfs()
        return result

# Iterative
class Solution:
    def lexicalOrder(self, n: int) -> list[int]:
        result = []
        num = 1

        for _ in range(n):
            result.append(num)

            if num * 10 <= n:
                num *= 10
            else:
                while num >= n or num % 10 == 9:
                    num //= 10
                num += 1

        return result
