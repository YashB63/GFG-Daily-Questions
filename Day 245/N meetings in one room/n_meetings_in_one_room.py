class Solution:
    def maximumMeetings(self,n,start,end):
        x=sorted(zip(start,end), key=lambda x:x[1])
    
        count=0
        last_count=0
        for i in range(n):
            if x[i][0]>last_count:
                count+=1
                last_count=x[i][1]
        return count