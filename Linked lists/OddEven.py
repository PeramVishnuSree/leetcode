# Given the head of a singly linked list, group all the nodes with odd indices together followed by the nodes
# with even indices, and return the reordered list.
# The first node is considered odd, and the second node is even, and so on.
# Note that the relative order inside both the even and odd groups should remain as it was in the input.
# You must solve the problem in O(1) extra space complexity and O(n) time complexity.


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def oddEvenList(self, head):
        arr = []
        cur = head
        if head is None or head.next is None:
            return head

        while cur is not None:
            arr.append(cur.val)
            cur = cur.next

        even = []
        odd = []
        for i in range(len(arr)):
            if (i + 1) % 2 == 0:
                even.append(arr[i])
            else:
                odd.append(arr[i])

        arr = odd + even

        head_ = None
        for i in arr:
            if head_ is None:
                head_ = ListNode(i)
                cur = head_

            else:
                cur.next = ListNode(i)
                cur = cur.next

        return head_