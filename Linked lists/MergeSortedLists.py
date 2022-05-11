class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, list1, list2) :
        cur1 = list1
        cur2 = list2
        head = None

        if cur1 is None and cur2 is None:
            return head
        elif cur1 is None:
            return cur2
        elif cur2 is None:
            return cur1

        while cur1 is not None and cur2 is not None:
            if cur1.val <= cur2.val:
                if head is None:
                    head = cur1
                    cur = head
                else:
                    cur.next = cur1
                    cur = cur.next
                cur1 = cur1.next

            else:
                if head is None:
                    head = cur2
                    cur = head
                else:
                    cur.next = cur2
                    cur = cur.next
                cur2 = cur2.next

        if cur1 is None:
            cur.next = cur2
        else:
            cur.next = cur1

        return head