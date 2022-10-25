# link: https://leetcode.com/problems/product-of-array-except-self/
# solution reference: https://www.youtube.com/watch?v=bNvIQI2wAjk

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # idea: ans[i] = product(nums:0~i-1) * product(nums:i+1~n)
        output = [1] + (len(nums)-1)*[0] # storing prefix product with base case = 1

        for i in range(1, len(nums)):
            output[i] = output[i-1] * nums[i-1]

        # calculate prefix product * postfix product, then update postfix value (base case = 1)
        post = 1
        for i in range(len(nums)-1, -1, -1):
            output[i] *= post
            post *= nums[i]
        return output
