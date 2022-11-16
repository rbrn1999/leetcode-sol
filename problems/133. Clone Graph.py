# link: https://leetcode.com/problems/clone-graph/

"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if node is None:
            return None

        def dfs(c_node, ref):
            for n in ref.neighbors:
                if n.val not in nodes:
                    n_node = Node(n.val)
                    nodes[n.val] = n_node
                    dfs(n_node, n)
                c_node.neighbors.append(nodes[n.val])

        root = Node(val=node.val)
        nodes = {root.val: root}
        dfs(root, node)

        return root

# iterative solution
class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if node is None:
            return None
        
        root = Node(val=node.val)
        nodes = {root.val: root}
        # dfs(root, node)
        
        stack = [(root, node)]
        while stack:
            curNode, ref = stack.pop()
            for ref_n in ref.neighbors:
                if ref_n.val not in nodes:
                    nNode = Node(ref_n.val)
                    nodes[ref_n.val] = nNode
                    stack.append((nNode, ref_n))
                curNode.neighbors.append(nodes[ref_n.val])
        

        return root