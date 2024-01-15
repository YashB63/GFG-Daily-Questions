class Solution:
	def longSubarrWthSumDivByK (self,arr,  n, K) : 
		
        mxl = 0
        ps = 0
        dis = {}
        
        for i in range(n):
            ps += arr[i]
            rem = ps % K
            if(rem == 0):
                mxl = max(mxl, i + 1)
            if(rem < 0):
                rem += K
            if(rem in dis):
                mxl = max(mxl, i - dis[rem])
            else:
                dis[rem] = i
        
        return mxl