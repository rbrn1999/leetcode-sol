# link: https://leetcode.com/problems/adding-two-negabinary-numbers/
# Given two numbers arr1 and arr2 in base -2, return the result of adding them together.

# Each number is given in array format:  as an array of 0s and 1s, from most significant bit to least significant bit.  For example, arr = [1,1,0,1] represents the number (-2)^3 + (-2)^2 + (-2)^0 = -3.  A number arr in array, format is also guaranteed to have no leading zeros: either arr == [0] or arr[0] == 1.

# Return the result of adding arr1 and arr2 in the same format: as an array of 0s and 1s with no leading zeros.

 

# Example 1:

# Input: arr1 = [1,1,1,1,1], arr2 = [1,0,1]
# Output: [1,0,0,0,0]
# Explanation: arr1 represents 11, arr2 represents 5, the output represents 16.
# Example 2:

# Input: arr1 = [0], arr2 = [0]
# Output: [0]
# Example 3:

# Input: arr1 = [0], arr2 = [1]
# Output: [1]
 

# Constraints:

# 1 <= arr1.length, arr2.length <= 1000
# arr1[i] and arr2[i] are 0 or 1
# arr1 and arr2 have no leading zeros

from typing import List

class Solution:
    def addNegabinary(self, arr1: List[int], arr2: List[int]) -> List[int]:
        # make arrs' length the same
        result = [0] * (max(len(arr1), len(arr2)))
        arr1 = [0] * (len(result) - len(arr1)) + arr1
        arr2 = [0] * (len(result) - len(arr2)) + arr2

        # add arr1 and arr2 to result
        for i in range(len(result)-1, -1, -1):
            carry = (result[i] + arr1[i] + arr2[i]) // 2
            result[i] = (result[i] + arr1[i] + arr2[i]) % 2
            # subtract carry to the next number cause their sign is different 
            # (...-+-+-+)
            if i==0:
                result = [-carry] + result
            else:
                result[i-1] -= carry

        # process the left carries
        while result[0] < 0:
            carry = -result[0]
            result[0] %= 2
            result = [carry] + result
            
        # get rid off leading zeros
        while result[0] == 0 and len(result) > 1:
            result = result[1:]
        return result


            
output = Solution().addNegabinary(arr1 = [1], arr2 = [1, 1])
print(output)