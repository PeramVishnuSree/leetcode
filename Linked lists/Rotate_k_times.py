# Given the head of a linked list, rotate the list to the right by k places.



class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:

    def rotateRight(self, head, k):
        cur = head
        l = 0
        temp = head
        while temp is not None:
            l += 1
            temp = temp.next

        if cur is None:
            return cur

        k = k % l

        if cur.next is None:
            return cur

        for i in range(k):
            cur = self.rotate(cur)

        return cur

    def rotate(self, head):
        cur = head
        while cur.next.next is not None:
            cur = cur.next

        temp = cur.next
        cur.next = None
        temp.next = head

        return temp