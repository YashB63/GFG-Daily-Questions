class Solution:
	def CountWays(self, s):
		
        mod = 10**9 + 7
        
        if s.startswith("0") or "00" in s:
            return 0
        
        dp = [0 for _ in range(len(s))]
        
        n = len(s)
        if n >= 1 and s[n-1] != "0":
            dp[n-1] = 1
       
        if n >= 2 and s[n-2] != "0" and int(s[n-2]+s[n-1]) <= 26:
            dp[n-2] = dp[n-1] + 1
        elif s[n-2] == "0":
            dp[n-2] = 0
        else:
            dp[n-2] = dp[n-1]
           

        for i in range(len(s)-3, -1, -1):
            curr_char = s[i]
            if curr_char == "0":
                dp[i] = 0
                continue
            
            next_char = s[i+1]
            
            
            if 1 <= int(curr_char + next_char) <= 26:
               dp[i] = (dp[i + 1] % mod + dp[i + 2] % mod) % mod
            else:
               dp[i] = dp[i+1] % mod
               
            
        return dp[0]