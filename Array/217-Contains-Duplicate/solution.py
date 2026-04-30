class Solution:
    def containsDuplicate(self, nums):
        # A set in Python uses a hash table for O(1) average time complexity lookups
        seen = set()
        
        for n in nums:
            if n in seen:
                return True
            seen.add(n)
            
        return False
