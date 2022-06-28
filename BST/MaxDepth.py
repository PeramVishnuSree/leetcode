
# Given the root a binary tree, find the maximum depth of the same tree

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxDepth(self, root):
        node = root
        if node is None:
            return 0

        else :

            # Compute the depth of each subtree
            l = self.maxDepth(node.left)
            r = self.maxDepth(node.right)

            # Use the larger one
            if (l > r):
                return l+1
            else:
                return r+1