class Solution:
    def wordBreak(self, s, wordDict):
        # Convert list to set for O(1) lookups
        word_set = set(wordDict)
        # dp[i] means s[:i] can be segmented
        dp = [False] * (len(s) + 1)
        dp[0] = True
        
        for i in range(1, len(s) + 1):
            for j in range(i):
                # If s[:j] is valid and s[j:i] is in the dictionary
                if dp[j] and s[j:i] in word_set:
                    dp[i] = True
                    break # No need to check other j's for this i
                    
        return dp[len(s)]
