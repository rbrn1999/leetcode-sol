# link: https://leetcode.com/problems/multiply-strings/

class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        num1 = [int(num) for num in num1[::-1]]
        num2 = [int(num) for num in num2[::-1]]
        
        result = [0]*(len(num1)+len(num2)+1)
        for i in range(len(num1)):
            [0]*(len(num1)+len(num2))
            for j in range(len(num2)):
                result[i+j] += num1[i]*num2[j]
                result[i+j+1] += result[i+j]//10
                result[i+j] %= 10
        while result[-1] == 0 and len(result) > 1:
            result = result[:-1]
        
        return ''.join([str(num) for num in result[::-1]])