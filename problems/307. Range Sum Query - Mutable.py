# link: https://leetcode.com/problems/range-sum-query-mutable/

class NumArray:
    class Node:
        def __init__(self, l: int, r: int, total: int=0):
            self.l = l
            self.r = r
            self.total = total
            self.left = None
            self.right = None


    def __init__(self, nums: list[int]):
        self.root = self.buildTree(nums, 0, len(nums)-1)


    def buildTree(self, nums: list[int], l: int, r: int) -> Node:
        root = self.Node(l, r)
        if l == r:
            root.total = nums[l]
            return root

        mid = (l + r) // 2

        leftNode = self.buildTree(nums, l, mid)
        rightNode = self.buildTree(nums, mid+1, r)
        root.left = leftNode
        root.right = rightNode
        root.total = leftNode.total + rightNode.total

        return root

    def update(self, index: int, val: int) -> None:
        def helper(node: self.Node):
            if node.l == node.r:
                node.total = val
                return val

            mid = (node.l + node.r) // 2
            if index <= mid:
                node.left.total = helper(node.left)
            else:
                node.right.total = helper(node.right)

            node.total = node.left.total + node.right.total
            return node.total

        helper(self.root)

    def sumRange(self, left: int, right: int) -> int:
        def helper(l, r, node):
            if node.l == l and node.r == r:
                return node.total

            mid = (node.l + node.r) // 2
            if r <= mid:
                return helper(l, r, node.left)
            if l > mid:
                return helper(l, r, node.right)

            return helper(l, mid, node.left) + helper(mid+1, r, node.right)

        return helper(left, right, self.root)


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(index,val)
# param_2 = obj.sumRange(left,right)
