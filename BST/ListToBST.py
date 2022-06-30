
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def sortedListToBST(self, head):

        l = []
        curr = head

        while (curr != None):
            l.append(curr.val)
            curr = curr.next

        def solve(l):
            if not l:
                return None
            mid = len(l) // 2
            root = TreeNode(l[mid])
            root.left = solve(l[:mid])
            root.right = solve(l[mid + 1:])
            return root

        return solve(l)
