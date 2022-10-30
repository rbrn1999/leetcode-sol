# link: https://leetcode.com/problems/height-of-binary-tree-after-subtree-removal-queries
# solution reference: https://leetcode.com/problems/height-of-binary-tree-after-subtree-removal-queries/discuss/2758013/

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
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
        