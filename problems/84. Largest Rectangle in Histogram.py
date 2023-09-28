# link: https://leetcode.com/problems/largest-rectangle-in-histogram/

class Solution:
    def largestRectangleArea(self, heights: list[int]) -> int:
        n = len(heights)
        width = [1] * n
        stack = []
        for i in range(n):
            while stack and heights[stack[-1]] >= heights[i]:
                stack.pop()
            j = stack[-1] if stack else -1
            stack.append(i)
            width[i] += i-1-j

        stack = []
        for i in range(n-1, -1, -1):
            while stack and heights[stack[-1]] >= heights[i]:
                stack.pop()
            j = stack[-1] if stack else n
            stack.append(i)
            width[i] += j-1-i
        
        max_area = 0
        for i in range(n):
            max_area = max(max_area, width[i] * heights[i])
        return max_area


class Solution:
    def largestRectangleArea(self, heights: list[int]) -> int:
        max_area = 0
        heights.append(0)
        stack = [] # (start_index, height) monotonic increasing stack
        for i in range(len(heights)):
            start = i
            while stack and stack[-1][1] > heights[i]:
                j, h = stack.pop()
                start = j
                max_area = max(max_area, h * (i-j))
            stack.append((start, heights[i]))

        return max_area  