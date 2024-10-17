# link: https://leetcode.com/problems/maximum-swap/
# You are given an integer num. You can swap two digits at most once to get the maximum valued number.

# Return the maximum valued number you can get.



# Example 1:

# Input: num = 2736
# Output: 7236
# Explanation: Swap the number 2 and the number 7.
# Example 2:

# Input: num = 9973
# Output: 9973
# Explanation: No swap.


# Constraints:

# 0 <= num <= 108

# Greedy, 2-pass
class Solution:
    def maximumSwap(self, num: int) -> int:
        arr = []
        temp_num = num
        while temp_num:
            arr.append(temp_num%10)
            temp_num //= 10

        # find the first digit that's accending
        i = len(arr)-1
        while i > 0 and arr[i] >= arr[i-1]:
            i -= 1

        # if the whole sequence is decending, no swap
        if i == 0:
            return num

        # find the largest digit after (including) the first accending digit
        r = i - 1
        for k in range(i-1, -1, -1):
            if arr[k] >= arr[r]:
                r = k

        # find the most significant position that has a digit smaller than the digit to swap
        l = i
        for k in range(len(arr)-1, i-1, -1):
            if arr[k] < arr[r]:
                l = k
                break

        arr[l], arr[r] = arr[r], arr[l]
        return sum(arr[i] * 10 ** i for i in range(len(arr)))


# Brute Force
class Solution:
    def maximumSwap(self, num: int) -> int:
        arr = []
        while num > 0:
            arr.insert(0, num % 10)
            num //= 10
        ptr = 0
        max_idx = 0
        des = True
        for i in range(len(arr)):
            if des and i>0 and arr[i]>arr[i-1]:
                des = False
                ptr = i
                max_idx = i
            if not des and i>0 and arr[i] >= arr[max_idx]:
                max_idx = i
        for i in range(0, ptr):
            if arr[max_idx] > arr[i]:
                arr[max_idx], arr[i] = arr[i], arr[max_idx]
                break
        s = ""
        for num in arr:
            s += str(num)
        return int(s)
