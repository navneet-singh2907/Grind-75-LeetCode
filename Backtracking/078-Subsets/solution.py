class Solution:
    def subsets(self, nums):
        res = []
        
        def backtrack(start, curr):
            # Every step in the recursion is a valid subset
            res.append(list(curr))
            
            for i in range(start, len(nums)):
                # 1. Action: Add the number
                curr.append(nums[i])
                
                # 2. Recurse: Move to the next index
                backtrack(i + 1, curr)
                
                # 3. Backtrack: Remove the number to try the next one
                curr.pop()
        
        backtrack(0, [])
        return res
