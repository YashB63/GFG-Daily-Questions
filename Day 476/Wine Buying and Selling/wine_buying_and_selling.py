class Solution:	
	def wineSelling(self, Arr, N):
        i = 0
        j = 0
        ans = 0
        while i < N and j< N:
            while i<N and Arr[i] <=0:
                i+=1
            while j<N and Arr[j] > 0:
                j+=1
            if i>=N or j>=N:
                break
            min1 = min(Arr[i],-Arr[j])
            Arr[i] -=  min1
            Arr[j] +=  min1
            ans += min1*abs(i-j)
            if Arr[i] == 0:
                i+=1
            if Arr[j] == 0:
                j+=1
        return ans