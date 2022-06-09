# Given the head of a singly linked list and two integers left and right where left <= right,
# reverse the nodes of the list from position left to position right, and return the reversed list.


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseBetween(self, head, left, right):

        if left == right or head == None or head.next == None:
            return head
        arr = []
        cur = head
        while cur is not None:
            arr.append(cur.val)
            cur = cur.next
        rr = arr[left - 1:right]
        rr.reverse()
        ans = arr[:left - 1] + rr + arr[right:]
        head_ = self.create(ans)
        return head_


    def create(self, array):
        head = None
        cur = None
        for i in array:
            if head is None:
                head = ListNode(i)
                cur = head
            else:
                cur.next = ListNode(i)
                cur = cur.next
        return head