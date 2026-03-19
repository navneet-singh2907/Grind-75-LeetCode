
class Solution:
    def diameterOfBinaryTree(self, root):
        self.max_diameter = 0
        
        def get_height(node):
            if not node:
                return 0
            
            # Recursively find the height of left and right subtrees
            left_h = get_height(node.left)
            right_h = get_height(node.right)
            
            # The diameter at the current node is the sum of left and right heights
            current_diameter = left_h + right_h
            
            # Update the global maximum diameter
            self.max_diameter = max(self.max_diameter, current_diameter)
            
            # Return the height of the current node to its parent
            return 1 + max(left_h, right_h)
            
        get_height(root)
        return self.max_diameter
