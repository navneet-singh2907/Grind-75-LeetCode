import bisect

class Solution:
    def jobScheduling(self, startTime, endTime, profit):
        # 1. Combine and sort jobs by end time
        jobs = sorted(zip(startTime, endTime, profit), key=lambda x: x[1])
        
        # 2. dp[i] = (end_time, max_profit) up to that time
        # Initialize with a dummy job ending at 0 with 0 profit
        dp = [(0, 0)]
        
        for s, e, p in jobs:
            # Find the last job that finished before the current job starts
            # We search for 's' in the list of end times stored in dp
            i = bisect.bisect_right(dp, (s, float('inf'))) - 1
            
            # Option: profit of previous non-overlapping job + current job profit
            current_total_profit = dp[i][1] + p
            
            # If taking this job increases our total max profit, add it to DP
            if current_total_profit > dp[-1][1]:
                dp.append((e, current_total_profit))
                
        return dp[-1][1]
