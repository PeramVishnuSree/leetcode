# Given the head of a linked list,
# remove the nth node from the end of the list and return its head.

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeNthFromEnd(self, head, n) :
        l = self.length(head)
        i = l - n
        if l <= 1:
            return None
        if i == 0:
            head = head.next
            return head

        cur = head
        for k in range(i - 1):
            cur = cur.next
        cur.next = cur.next.next
        return head

    def length(self, head):
        i = 0
        cur = head
        while cur is not None:
            i += 1
            cur = cur.next

        return i