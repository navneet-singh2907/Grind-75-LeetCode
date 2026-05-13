class Solution:
    def buildTree(self, preorder, inorder):
        # Map values to their indices in inorder for O(1) lookup
        inorder_map = {val: i for i, val in enumerate(inorder)}
        self.pre_idx = 0
        
        def helper(left, right):
            if left > right:
                return None
            
            # Select the current root from preorder
            root_val = preorder[self.pre_idx]
            root = TreeNode(root_val)
            self.pre_idx += 1
            
            # Split the inorder array into left and right subtrees
            mid = inorder_map[root_val]
            
            # Recursively build
            root.left = helper(left, mid - 1)
            root.right = helper(mid + 1, right)
            
            return root
            
        return helper(0, len(inorder) - 1)
