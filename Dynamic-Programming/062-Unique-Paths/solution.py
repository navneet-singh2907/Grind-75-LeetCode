class Solution:
    def uniquePaths(self, m, n):
        # Use a single row to save space O(n)
        row = [1] * n
        
        for i in range(1, m):
            for j in range(1, n):
                # New value = top value + left value
                row[j] += row[j - 1]
                
        return row[-1]
