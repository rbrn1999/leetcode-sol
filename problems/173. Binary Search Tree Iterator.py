# link: https://leetcode.com/problems/binary-search-tree-iterator/

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from typing import Optional
class BSTIterator:
    root = None
    cur = root
    s = []
    def __init__(self, root: Optional[TreeNode]):
        self.root = root
        self.cur = root
    def next(self) -> int:
        while self.s or self.cur:
            if self.cur:
                self.s.append(self.cur)
                self.cur = self.cur.left
            else:
                self.cur = self.s.pop()
                value = self.cur.val
                self.cur = self.cur.right
                return value
                

    def hasNext(self) -> bool:
        return self.s or self.cur


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()