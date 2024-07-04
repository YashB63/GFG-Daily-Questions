class Solution:
    
    #Function to find length of longest increasing subsequence.
    def longestSubsequence(self, n, a):
        
        b = []
        bl = 0
        for i in range(n):
            if not b:
                b.append(a[i])
                bl+=1
                continue
            if b[-1] < a[i]:
                b.append(a[i])
                bl+=1
            else:
                for j in range(bl):
                    if b[j] == a[i]:
                        break
                    if b[j]>a[i]:
                        b[j] = a[i]
                        break
        
        return bl