# Given a linked list, swap every two adjacent nodes and return its head.
# You must solve the problem without modifying the values in the list's nodes
# (i.e., only nodes themselves may be changed.)


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:

    def swapPairs(self, head):
        cur = head
        prev = None
        if head is None:
            return None
        if head.next is None:
            return head
        head = None
        while cur.next is not None:
            temp = cur.next
            if head is None:
                head = temp
            cur.next = cur.next.next
            if prev is not None:
                prev.next = temp
            temp.next = cur
            prev = cur
            cur = cur.next
            if cur is None:
                break
        return head