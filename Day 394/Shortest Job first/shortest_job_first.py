class Solution:
    def solve(self, bt):
        bt.sort()
        
        waiting_time = 0
        total_waiting_time = 0
        
        for i in range(len(bt)):
            total_waiting_time += waiting_time
            waiting_time +=bt[i]
        
        average_waiting_time = total_waiting_time // len(bt)
        
        return average_waiting_time