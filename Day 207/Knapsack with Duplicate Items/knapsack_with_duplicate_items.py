class Solution:
    def knapSack(self, N, W, val, wt):
        
        a = []
        b = []
        for i in range(W+1):
            curr = val[0]*(i//wt[0]) if i>=wt[0] else 0
            a.append(curr)
        b = a
        for i in range(1, N):
            for j in range(1, W+1):
                if wt[i] <= j:
                    curr = max(val[i] + b[j-wt[i]], a[j])
                    b[j] = curr
                else:
                    b[j] = a[j]
            a = b
        return b[-1]