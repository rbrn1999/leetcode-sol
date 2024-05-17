# link: https://leetcode.com/problems/strobogrammatic-number-ii/

class Solution:
    def findStrobogrammatic(self, n: int) -> list[str]:
        number_map = {'0': '0', '1': '1', '8': '8', '6': '9', '9': '6'}
        mids = {'0', '1', '8'}
        num_str = ['_'] * n
        result = []

        def helper(i: int) -> None:
            if i == (n // 2 + n % 2):
                result.append(''.join(num_str))
                return

            if n % 2 == 1 and i == n // 2:
                for num in mids:
                    num_str[i] = num
                    helper(i+1)

                return

            for num in number_map:
                if i == 0 and num == '0':
                    continue
                num_str[i] = num
                num_str[n-1-i] = number_map[num]
                helper(i+1)

        helper(0)
        return result
