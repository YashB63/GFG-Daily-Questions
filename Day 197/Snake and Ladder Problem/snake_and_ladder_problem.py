class Solution:
    def minThrow(self, N, arr):
        
        SL = {}
        target = 30
        
        for i in range(0,2*N,2) :
            SL[arr[i]] = arr[i+1]
            
        q = [(1,0)]
        
        vis = [False] * (target+1)
            
            
        while q :
            pos, roll = q.pop(0)
            
            if pos == target :
                return roll
                
            for i in range(1,7):
                newpos = pos + i
                if newpos in SL :
                    newpos = SL[newpos]
                        
                if newpos <= target and vis[newpos] == False :
                    q.append((newpos,roll+1))
                    vis[newpos] = True