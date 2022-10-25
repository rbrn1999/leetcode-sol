# link: https://leetcode.com/problems/serialize-and-deserialize-binary-tree/

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

from collections import deque
class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        if root is None:
            return ""
        cur = deque([root])
        nxt = deque()
        nodes = []
        while cur:
            node = cur.popleft()
            nodes.append(node)
            if node:
                nxt.extend([node.left, node.right])
            if len(cur) == 0:
                cur, nxt = nxt, deque()
        s = [str(node.val) if node is not None else '_' for node in nodes]
        return ' '.join(s)


    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        if data == "":
            return None

        vals = data.split()
        root = TreeNode(int(vals[0]))
        parents = deque([root])
        status = 0 # 0: append left -> 1: append right -> go to next parent node and reset

        for i in range(1, len(vals)):
            node = None
            if vals[i] != "_":
                node = TreeNode(int(vals[i]))
                parents.append(node)
            if status == 0:
                parents[0].left = node
                status = 1
            elif status == 1:
                parents[0].right = node
                parents.popleft()
                status = 0
            else:
                print("should never happen")

        return root




# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))
