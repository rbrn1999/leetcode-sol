# link: https://leetcode.com/problems/flatten-a-multilevel-doubly-linked-list/

# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child

from typing import Optional
class Solution:
    def flatten(self, head: 'Optional[Node]') -> 'Optional[Node]':
        def traverse(node):
            prev = None
            while node and node.child is None:
                prev = node
                node = node.next
                
            if node is None:
                return prev
            
            childEnd = traverse(node.child)
            if node.next is not None:
                node.next.prev, childEnd.next = childEnd, node.next
            node.next, node.child.prev = node.child, node
            node.child = None
            return traverse(childEnd.next if childEnd.next is not None else childEnd)
        
        traverse(head)
        return head