# given the head of a linked list, return true if it has a cycle in it  or false otherwise.

class Solution:
    def hasCycle(self, head) :
        fast = head
        slow = head
        while fast is not None:
            if fast is None or fast.next is None:
                return False
            if fast.next.next == slow:
                return True
            fast = fast.next.next
            slow = slow.next

        return False