# link: https://leetcode.com/problems/height-of-binary-tree-after-subtree-removal-queries

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import defaultdict
class Solution:
    def treeQueries(self, root: Optional[TreeNode], queries: List[int]) -> List[int]:
        maxHeightAfterRemoval = defaultdict(int)

        def left_to_right_dfs(root: Optional[TreeNode], cur_height: int=0, max_height: int=0) -> int:
            if root is None:
                return 0

            # using preorder traversal so the whole subtree of 'root' is not processed (max height is not computed based on those nodes)
            maxHeightAfterRemoval[root.val] = max(maxHeightAfterRemoval[root.val], max_height)
            max_height = max(max_height, cur_height)

            max_height = max(left_to_right_dfs(root.left, cur_height+1, max_height), max_height)
            max_height = max(left_to_right_dfs(root.right, cur_height+1, max_height), max_height)
            return max_height

        def right_to_left_dfs(root: Optional[TreeNode], cur_height: int=0, max_height: int=0) -> int:
            if root is None:
                return 0

            # using preorder traversal so the whole subtree of 'root' is not processed (max height is not computed based on those nodes)
            maxHeightAfterRemoval[root.val] = max(maxHeightAfterRemoval[root.val], max_height)
            max_height = max(max_height, cur_height)

            max_height = max(right_to_left_dfs(root.right, cur_height+1, max_height), max_height)
            max_height = max(right_to_left_dfs(root.left, cur_height+1, max_height), max_height)
            return max_height

        left_to_right_dfs(root)
        right_to_left_dfs(root)
        return [maxHeightAfterRemoval[q] for q in queries]

# solution reference: https://leetcode.com/problems/height-of-binary-tree-after-subtree-removal-queries/discuss/2758013/
class Solution:
    def treeQueries(self, root: Optional[TreeNode], queries: List[int]) -> List[int]:
        depths = {}
        heights = {}
        top2Heights = defaultdict(lambda: [-1, -1]) # minimum hight of root is 0, so set default(null nodes) to -1
        def dfs(node, depth=0) -> int: # retrun height
            if node is None:
                return -1
            height = max(dfs(node.left, depth+1), dfs(node.right, depth+1)) + 1
            depths[node.val] = depth
            heights[node.val] = height
            top2Heights[depth][1] = max(top2Heights[depth][1], height)
            top2Heights[depth].sort(reverse=True)
            return height


        dfs(root)
        res = []
        for q in queries:
            height = top2Heights[depths[q]][0] if heights[q] < top2Heights[depths[q]][0] else top2Heights[depths[q]][1]
            res.append(depths[q] + height)

        return res
