# link: https://leetcode.com/problems/expression-add-operators/

class Solution:
    def addOperators(self, num: str, target: int) -> list[str]:
        num_arr = [''] * (len(num) + len(num)-1)
        for i, num in enumerate(num):
            num_arr[i*2] = num
        
        result = []
        ops = ['+', '-', '*']
        def helper(i: int) -> None:
            if i >= len(num_arr):
                s = ''.join(num_arr)
                if eval(s) == target:
                    result.append(s)
                return
            
            if num_arr[i-1] != '0' or i-2 >= 0 and num_arr[i-2] == '':
                helper(i+2)

            for op in ops:
                num_arr[i] = op
                helper(i+2)

            num_arr[i] = ''
        
        helper(1)
        return result