class Solution:
    def smallestSumSubarray(self, A, N):
        current_sum=0
        min_sum=A[0]
        for i in range(N):
            current_sum+=A[i]
            min_sum=min(current_sum,min_sum)
            if current_sum>0:
                current_sum=0
        return min_sum