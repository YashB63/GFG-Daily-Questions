class Solution:

    def transform(self, S):
        
        stack = []
        arr = []
        S = S.lower()
        i = 0
        n = len(S)
        i = 0
        n = len(S)
        while i < n:
            count = 1
            while i < n - 1 and S[i] == S[i + 1]:
                count += 1
                i += 1
                
            arr.append(str(count))
            arr.append(S[i])
            i += 1
        
        return ''.join(arr)