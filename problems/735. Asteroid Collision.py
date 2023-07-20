# link: https://leetcode.com/problems/asteroid-collision/

class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        for asteroid in asteroids:
            if asteroid > 0:
                stack.append(asteroid)
            else:
                exist = True
                while stack and stack[-1] and stack[-1] > 0:
                    if stack[-1] > abs(asteroid):
                        exist = False
                        break
                    if stack[-1] == abs(asteroid):
                        stack.pop()
                        exist = False
                        break
                    if stack[-1] < abs(asteroid):
                        stack.pop()
                if exist:
                    stack.append(asteroid)

        return stack

