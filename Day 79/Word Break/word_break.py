class Solution:
    def wordBreak(self, n, s, dictionary):
        
        n = len(s)
        x = [False] * (n + 1)
        x[0] = True
        
        mx = max(len(word) for word in dictionary)

        for i in range(1, n+1):
            for j in range(max(0, i - mx), i):
                if x[j] and s[j:i] in dictionary:
                    x[i] = True
                    break
                
        return 1 if x[n] else 0