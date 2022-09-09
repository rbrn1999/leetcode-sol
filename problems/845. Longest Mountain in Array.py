# link: https://leetcode.com/problems/longest-mountain-in-array/submissions/

class Solution:
    def longestMountain(self, arr: list[int]) -> int:
        if len(arr) < 3:
            return 0
        
        arr.append(arr[-1]) # makes the loop able to record the mountain ends at arr[-1]
        counting = asc = arr[1] > arr[0] # "counting" for identifying if we are keeping track of a valid mountain 
        longest = 0
        start = 0 # index
        
        for i in range(1, len(arr)):
            if asc and arr[i] < arr[i-1]:
                asc = False
            elif not asc and arr[i] > arr[i-1]: # stop descending(or going flat) and start ascending
                if counting:
                    longest = max((i-1)-start+1, longest)
                asc = counting = True
                start = i-1
            elif arr[i] == arr[i-1]:
                if not asc and counting:
                    longest = max((i-1)-start+1, longest)
                asc = counting = False
                start = i
                
        return longest