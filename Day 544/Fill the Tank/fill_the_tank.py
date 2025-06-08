from collections import deque

class Solution:
    def minimum_amount(self,Edges,num, start,cap):
        def check(gr,num,start,cap,water):
            vis=[0]*100010
            q=deque()
            q.append([start,water])
            
            while(q):
                val=q.popleft()
                curr=val[0]
                curr_water=val[1]
                vis[curr]=1
        
                if (cap[curr-1]>curr_water):
                    return 0
                
                curr_water-=cap[curr-1]
                
                neighbour=0
                
                for it in gr[curr]:
                    nxt=it
                    if(vis[nxt]==0):
                        neighbour+=1  
              
                if(neighbour>0):
                    curr_water=(curr_water//neighbour)
                
                for it in gr[curr]:
                    nxt=it
                    if(vis[nxt]==0):
                        q.append([nxt,curr_water])
            
            return 1
        
        hi=10**18+1
        lo=0
        maxx=10**18+1
        gr=[[] for i in range(100011)]

        for i in range(num-1):
            gr[Edges[i][0]].append(Edges[i][1])
            gr[Edges[i][1]].append(Edges[i][0])
       
        while(hi>=lo):
            mid=(hi+lo)//2
            
            if(mid>=maxx):
                return -1
            
            if(check(gr,num,start,cap,mid)==0):
                lo=mid+1
            else:
                hi=mid-1
        
        return lo