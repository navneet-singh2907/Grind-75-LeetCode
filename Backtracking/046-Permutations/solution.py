class Solution:
    def permute(self, nums):
        res = []
        used = set()
        
        def backtrack(curr):
            # Base Case: Current permutation is complete
            if len(curr) == len(nums):
                res.append(list(curr))
                return
            
            for n in nums:
                if n not in used:
                    # Action: Add number and mark as used
                    used.add(n)
                    curr.append(n)
                    
                    # Recurse
                    backtrack(curr)
                    
                    # Backtrack: Remove number and unmark
                    curr.pop()
                    used.remove(n)
                    
        backtrack([])
        return res
