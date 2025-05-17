class Solution:
    def querySum(self, n, arr, q, queries):
        pre = [0] * n
        pre[0] = arr[0]
        
        for i in range(1, n):
            pre[i] = pre[i - 1] + arr[i]

        sol = []

        for i in range(0, 2 * q, 2):
            l = queries[i]
            r = queries[i + 1]
            if l == 1:
                sol.append(pre[r - 1])  
            else:
                sol.append(pre[r - 1] - pre[l - 2])  

        return sol