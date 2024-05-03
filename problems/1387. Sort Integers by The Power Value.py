# link: https://leetcode.com/problems/sort-integers-by-the-power-value/

class Solution:
    def getKth(self, lo: int, hi: int, k: int) -> int:
        num_steps = [0] * (hi-lo+1)

        for i in range(hi-lo+1):
            num = lo + i
            steps = 0
            while num != 1:
                if num % 2 == 0:
                    num //= 2
                else:
                    num = num * 3 + 1
                steps += 1

            num_steps[i] = steps

        pairs = [(steps, i+lo) for i, steps in enumerate(num_steps)]
        pairs.sort()

        return pairs[k-1][1]
