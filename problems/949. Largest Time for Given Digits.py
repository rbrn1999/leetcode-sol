# link: https://leetcode.com/problems/largest-time-for-given-digits/

class Solution:
    def largestTimeFromDigits(self, arr: list[int]) -> str:
        # 2 as the first digit
        if 2 in arr:
            i = arr.index(2)
            arr[0], arr[i] = arr[i], arr[0]

            i = -1
            for j in range(1, 4):
                if arr[j] < 4 and (i == -1 or arr[j] > arr[i]):
                    i = j   
            if i == -1:
                i = 1

            arr[i], arr[1] = arr[1], arr[i]
            if arr[2] > 5:
                arr[2], arr[3] = arr[3], arr[2]
            elif arr[2] < arr[3] and arr[3] < 6:
                arr[2], arr[3] = arr[3], arr[2]

            if arr[0] * 10 + arr[1] < 24 and arr[2] * 10 + arr[3] < 60:
                return str(arr[0]) + str(arr[1]) + ':' + str(arr[2]) + str(arr[3])

        # if the above is not valid, try 0 or 1 as the first digit
        if 1 in arr:
            i = arr.index(1)
            arr[0], arr[i] = arr[i], arr[0]
        elif 0 in arr:
            i = arr.index(0)
            arr[0], arr[i] = arr[i], arr[0]
        else:
            return ""
        
        i = 1
        for j in range(2, 4):
            if arr[j] > arr[i]:
                i = j       

        arr[1], arr[i] = arr[i], arr[1] 
        if arr[2] > 5:
            arr[2], arr[3] = arr[3], arr[2]
        elif arr[2] < arr[3] and arr[3] < 6:
            arr[2], arr[3] = arr[3], arr[2]
        
        if arr[2] < 6:
            return str(arr[0]) + str(arr[1]) + ':' + str(arr[2]) + str(arr[3])
        
        return ""
