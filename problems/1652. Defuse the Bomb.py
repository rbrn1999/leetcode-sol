# link: https://leetcode.com/problems/defuse-the-bomb/

class Solution:
    def decrypt(self, code: list[int], k: int) -> list[int]:
        n = len(code)
        result = []
        if k == 0:
            return [0] * n
        if k < 0:
            cur = 0
            k *= -1
            for i in range(n-k, n):
                cur += code[i]
            result.append(cur)
            for i in range(1, n):
                cur -= code[(i-k-1+n)%n]
                cur += code[i-1]
                result.append(cur)
        else:
            cur = 0
            for i in range(1, 1+k):
                cur += code[i%n]
            result.append(cur)
            for i in range(1, n):
                cur -= code[i]
                cur += code[(i+k)%n]
                result.append(cur)

        return result
