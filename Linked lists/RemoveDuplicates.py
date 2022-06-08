# Given the head of a sorted linked list, delete all nodes that have duplicate numbers,
# leaving only distinct numbers from the original list. Return the linked list sorted as well.


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def deleteDuplicates(self, head):
        cur = head
        arr = []
        duplicates = []
        while cur is not None:
            if cur.val in arr:
                duplicates.append(cur.val)
                arr.remove(cur.val)
            elif cur.val in duplicates:
                pass
            else:
                arr.append(cur.val)
            cur = cur.next

        return self.create(arr)

    def create(self, array):
        head = None
        cur = None
        for i in array:
            if head is None:
                head = ListNode(i)
                cur = head
                continue
            else:
                cur.next = ListNode(i)
                cur = cur.next

        return head