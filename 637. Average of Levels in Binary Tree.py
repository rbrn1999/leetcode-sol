# link: https://leetcode.com/problems/average-of-levels-in-binary-tree/

Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        curLvl = [root]
        curLvlVals = []
        nxtLvl = []

        result = []

        while len(curLvl) > 0:
            cur = curLvl.pop(0)
            curLvlVals.append(cur.val)
            if cur.left is not None:
                nxtLvl.append(cur.left)
            if cur.right is not None:
                nxtLvl.append(cur.right)

            if len(curLvl) == 0:
                result.append(sum(curLvlVals)/len(curLvlVals))
                curLvl = nxtLvl
                nxtLvl, curLvlVals = [], []

        return result
