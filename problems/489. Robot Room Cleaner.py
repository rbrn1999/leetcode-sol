# link: https://leetcode.com/problems/robot-room-cleaner/

# """
# This is the robot's control interface.
# You should not implement it, or speculate about its implementation
# """
#class Robot:
#    def move(self):
#        """
#        Returns true if the cell in front is open and robot moves into the cell.
#        Returns false if the cell in front is blocked and robot stays in the current cell.
#        :rtype bool
#        """
#
#    def turnLeft(self):
#        """
#        Robot will stay in the same cell after calling turnLeft/turnRight.
#        Each turn will be 90 degrees.
#        :rtype void
#        """
#
#    def turnRight(self):
#        """
#        Robot will stay in the same cell after calling turnLeft/turnRight.
#        Each turn will be 90 degrees.
#        :rtype void
#        """
#
#    def clean(self):
#        """
#        Clean the current cell.
#        :rtype void
#        """

class Solution:
    def cleanRoom(self, robot):
        """
        :type robot: Robot
        :rtype: None
        """
        cleaned = set()
        obstacles = set()

        dirs = [(0, -1), (1, 0), (0, 1), (-1, 0)]
        direction = 0 # [0, 3]
        def dfs(r, c, d):
            robot.clean()
            cleaned.add((r, c))

            for i in range(4):
                dr, dc = dirs[(d+i)%4]
                nr, nc = r+dr, c+dc
                if (nr, nc) not in cleaned and (nr, nc) not in obstacles:
                    if robot.move():
                        dfs(nr, nc, (d+i)%4)
                    else:
                        obstacles.add((nr, nc))

                robot.turnRight()
            
            # go back
            robot.turnLeft()
            robot.turnLeft()
            robot.move()
            robot.turnLeft()
            robot.turnLeft()
        
        dfs(0, 0, 0)
        