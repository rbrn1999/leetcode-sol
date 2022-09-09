# link: https://leetcode.com/problems/palindrome-linked-list/
# solution: https://leetcode.com/problems/palindrome-linked-list/discuss/1137027/

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        slow = fast = head

        # move slow to mid point
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # reverse the 2nd half of list
        prev = None
        while slow:
            slow.next, prev, slow = prev, slow, slow.next

        # check from both ends
        fast, slow = head, prev

        while slow:
            if fast.val != slow.val:
                return False
            fast, slow = fast.next, slow.next

        return True
