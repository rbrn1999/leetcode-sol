# link: https://leetcode.com/problems/number-of-steps-to-reduce-a-number-in-binary-representation-to-one/

class Solution:
    def numSteps(self, s: str) -> int:
        steps = 0
        carry = 0
        for digit in s[len(s)-1:0:-1]:
            if digit == '0':
                if carry:
                    steps += 2
                else:
                    steps += 1
            else:
                if carry:
                    steps += 1
                else:
                    steps += 2
                    carry = 1
        
        if carry: # '10'
            return steps + 1
        else: # '1'
            return steps 