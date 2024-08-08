class Solution:
	def editDistance(self, word1, word2):
		
        len1 = len(word1)
        len2 = len(word2)
        
        dp = [[0 if j > 0 and i > 0 else j if i == 0 else i for j in range(len1 + 1)] 
              for i in range(len2 + 1)]
        
        for i in range(1, len2 + 1):
            for j in range(1, len1 + 1):
                if word1[j - 1] == word2[i - 1]:
                    dp[i][j] = dp[i - 1][j - 1]
                else:
                    dp[i][j] = min(dp[i - 1][j - 1], dp[i][j - 1], dp[i - 1][j]) + 1
        
        return dp[-1][-1]