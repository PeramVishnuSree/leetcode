# You are given the head of a singly linked-list. The list can be represented as:
# L0 → L1 → … → Ln - 1 → Ln
# Reorder the list to be on the following form:
# L0 → Ln → L1 → Ln - 1 → L2 → Ln - 2 → …
# You may not modify the values in the list's nodes. Only nodes themselves may be changed.


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reorderList(self, head):
        """
        Do not return anything, modify head in-place instead.
        """

        if head is None or head.next is None:
            return head

        stack = []
        cur = head
        while cur is not None:
            stack.insert(0, cur)
            cur = cur.next

        cur = head
        for i in stack:
            if i == cur.next:
                cur.next = i
                i.next = None
                return head
            if i == cur:
                cur.next = None
                return head
            i.next = cur.next
            cur.next = i
            cur = i.next

        return head
