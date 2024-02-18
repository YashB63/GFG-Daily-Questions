class Solution:
    
    def maximumMeetings(self,n,start,end):
        
        schedule = list(zip(start, end))
        
        schedule.sort(key = lambda x: x[1])
        
        prev_end_time = schedule[0][1]
        count = 1
        
        for i in range(1, len(schedule)):
            if schedule[i][0] > prev_end_time:
                count += 1
                prev_end_time = schedule[i][1]
            else:
                pass
        return count