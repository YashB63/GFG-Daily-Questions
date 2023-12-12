class Solution:
    def leaders(self, A, N):
        leaders = []
        max_right = A[N - 1]
        leaders.append(max_right)
        
        for i in range(N - 2, -1, -1):
            if A[i] >= max_right:
                max_right = A[i]
                leaders.append(max_right)
                
        leaders.reverse()
        return leaders