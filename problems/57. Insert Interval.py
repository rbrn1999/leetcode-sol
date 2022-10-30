# link: https://leetcode.com/problems/insert-interval/

# solution reference: https://youtu.be/A8NUOmlwOlM
class Solution:
    def insert(self, intervals: list[list[int]], newInterval: list[int]) -> list[list[int]]:
        res = []
        
        for i in range(len(intervals)):
            if newInterval[1] < intervals[i][0]:
                res.append(newInterval)
                return res + intervals[i:]
            elif newInterval[0] > intervals[i][1]:
                res.append(intervals[i])
            else: # overlapping
                newInterval = [min(newInterval[0], intervals[i][0]), max(newInterval[1], intervals[i][1])]
        
        res.append(newInterval)
        
        return res

# class Solution:
#     def insert(self, intervals: list[list[int]], newInterval: list[int]) -> list[list[int]]:
        
#         l = r = -1
#         n = len(intervals)
        
#         if n == 0:
#             return [newInterval]
            
#         for i in range(n):
#             if newInterval[0] < intervals[i][0]:
#                 l = i-1
#                 break
#         for i in range(n):
#             if newInterval[1] < intervals[i][0]:
#                 r = i-1
#                 break
        
        
#         if newInterval[0] >= intervals[-1][0]:
#             l = r = n-1
#         elif newInterval[1] >= intervals[-1][0]:
#             r = n-1
        
        
#         if r == -1:
#             return [newInterval] + intervals            
#         elif l == n-1:
#             if newInterval[0] <= intervals[-1][1]:
#                 intervals[-1][1] = max(intervals[-1][1], newInterval[1])
#             else:
#                 return intervals + [newInterval]
#         elif l == r:
#             if newInterval[0] <= intervals[l][1] and newInterval[1] > intervals[l][1]:
#                 intervals[l][1] = newInterval[1]
#             elif newInterval[0] > intervals[l][1]:
#                 intervals.insert(l+1, newInterval)
#         else:
#             if l == -1:
#                 intervals[:r+1] = [[newInterval[0], max(intervals[r][1], newInterval[1])]]
#             elif newInterval[0] <= intervals[l][1]:
#                 intervals[l:r+1] = [[intervals[l][0], max(intervals[r][1], newInterval[1])]]
#             else:
#                 intervals[l+1:r+1] = [[newInterval[0], max(intervals[r][1], newInterval[1])]]
        
#         return intervals