# You are given two non-empty linked lists representing two non-negative integers.
# The digits are stored in reverse order, and each of their nodes contains a single digit.
# Add the two numbers and return the sum as a linked list.
# You may assume the two numbers do not contain any leading zero, except the number 0 itself.

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1, l2):
        str1 = ''
        str2 = ''
        cur = l1
        while cur is not None:
            str1 = str(cur.val)+str1
            cur = cur.next
        cur = l2
        while cur is not None:
            str2 = str(cur.val)+str2
            cur = cur.next
        ans = str(int(str1)+int(str2))
        ans = list(ans)
        ans.reverse()
        l = ListNode()
        l.val = ans[0]
        head = l
        for i in ans[1:]:
            l.next = ListNode(i)
            l = l.next
        return head