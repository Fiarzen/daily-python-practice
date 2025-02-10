class Solution(object):
    def countBits(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        ans = [bin(i).count('1') for i in range(n+1)]
    
    def optimised_countBits(self, n):
        dp = [0] * (n + 1)  # Initialize DP array
        
        for i in range(1, n + 1):
            dp[i] = dp[i >> 1] + (i & 1)  # Right shift and check last bit
        
        return dp        