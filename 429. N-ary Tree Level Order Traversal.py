# link: https://leetcode.com/problems/n-ary-tree-level-order-traversal/

# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children

class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        if root is None:
            return []
        result = [[root]]
        i = j = 0
        while len(result[i]) > j:
            if j == 0:
                result.append(list())
            result[i+1] += result[i][j].children
            if j == len(result[i])-1:
                result[i] = [node.val for node in result[i]]
                i += 1
                j = 0
            else:
                j += 1


        return result[:-1]
