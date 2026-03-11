class Solution:
    def trap(self, height):
        if not height:
            return 0
            
        l, r = 0, len(height) - 1
        left_max, right_max = height[l], height[r]
        res = 0
        
        while l < r:
            if left_max < right_max:
                l += 1
                left_max = max(left_max, height[l])
                # Water trapped is the current max minus the current bar height
                res += left_max - height[l]
            else:
                r -= 1
                right_max = max(right_max, height[r])
                # Water trapped is the current max minus the current bar height
                res += right_max - height[r]
                
        return res
