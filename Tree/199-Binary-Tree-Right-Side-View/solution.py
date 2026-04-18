
class Solution:
    def rightSideView(self, root):
        if not root:
            return []
        
        res = []
        queue = deque([root])
        
        while queue:
            level_length = len(queue)
            
            for i in range(level_length):
                node = queue.popleft()
                
                # If this is the last node in the current level, it's visible from the right
                if i == level_length - 1:
                    res.append(node.val)
                
                # Add children for the next level
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                    
        return res
