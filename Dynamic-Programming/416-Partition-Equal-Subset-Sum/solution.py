class Solution:
    def canPartition(self, nums):
        total_sum = sum(nums)
        
        # If the sum is odd, it's impossible to split into two equal integers
        if total_sum % 2 != 0:
            return False
        
        target = total_sum // 2
        # Use a set to store all reachable sums
        dp = {0}
        
        for n in nums:
            new_sums = set()
            for s in dp:
                if s + n == target:
                    return True
                if s + n < target:
                    new_sums.add(s + n)
            # Update our possible sums set
            dp.update(new_sums)
            
        return target in dp
