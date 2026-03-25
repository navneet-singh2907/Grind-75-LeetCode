class Solution:
    def sortColors(self, nums):
        # Initialize three pointers
        l, m = 0, 0
        h = len(nums) - 1
        
        while m <= h:
            if nums[m] == 0:
                # Swap 0 to the left
                nums[l], nums[m] = nums[m], nums[l]
                l += 1
                m += 1
            elif nums[m] == 1:
                # 1 is already in the middle, just move forward
                m += 1
            else: # nums[m] == 2
                # Swap 2 to the right
                nums[m], nums[h] = nums[h], nums[m]
                h -= 1
               
