class Solution:
    def largestRectangleArea(self, heights):
        # Add a sentinel value of 0 to flush the stack at the end
        heights.append(0)
        stack = [-1] # Initialize with -1 to handle width calculation easily
        max_area = 0
        
        for i in range(len(heights)):
            # While the current height is less than the height at stack's top
            while stack[-1] != -1 and heights[stack[-1]] >= heights[i]:
                # Pop the height and calculate area with i as the right boundary
                h = heights[stack.pop()]
                w = i - stack[-1] - 1
                max_area = max(max_area, h * w)
            
            stack.append(i)
            
        # Clean up heights for any potential re-use (sentinel removal)
        heights.pop()
        return max_area
