class Solution:
    
    def tour(self,lis, n):
       
        total = 0
        net=0
        start = 0
        for i in range(n):
            total+= lis[i][0]-lis[i][1]
            net += lis[i][0]-lis[i][1]
            if net<0:
                net=0
                start = i+1
        if total>=0:
            return start
        else:
            return -1