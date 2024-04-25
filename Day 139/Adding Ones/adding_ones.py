class Solution:
    def update(self, a, n, updates, k):
        
        for i in updates:
            a[i-1] += 1
        for i in range(1,n):
            a[i] += a[i-1]