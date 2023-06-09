# link: https://leetcode.com/problems/can-make-arithmetic-progression-from-sequence/

class Solution:
    def canMakeArithmeticProgression(self, arr: list[int]) -> bool:
        n = len(arr)
        minNum = float('inf')
        maxNum = -float('inf')
        for num in arr:
            minNum = min(minNum, num)
            maxNum = max(maxNum, num)
        if (maxNum - minNum) % (n-1) != 0:
            return False
        if maxNum == minNum:
            return True
        diff = (maxNum - minNum) // (n-1)
        i = 0
        while i < n:
            if (arr[i] - minNum) % diff != 0:
                return False

            j = (arr[i] - minNum) // diff
            if i == j:
                i += 1
            elif arr[i] == arr[j]: # duplicate element when diff != 0
                return False
            else:
                arr[i], arr[j] = arr[j], arr[i]

        return True
    