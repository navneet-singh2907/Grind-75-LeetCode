
class Solution:
    def maxDepth(self, root):
        # Base case: an empty node has depth 0
        if not root:
            return 0
        
        # Recursive relation: 1 (current node) + max depth of children
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))
