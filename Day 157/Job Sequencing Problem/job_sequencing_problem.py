class Solution:
    
    def JobScheduling(self,Jobs,n):
        
        Jobs.sort(key = lambda x : x.profit, reverse = True )
        
        maximum = max(job.deadline for job in Jobs)
        res = [-1] * (maximum + 1)
        
        profit = 0
        ids = 0
        
        for job in Jobs:
            for j in range(job.deadline, 0, -1):
                if res[j] ==-1:
                    res[j] = job.id
                    ids +=1
                    profit += job.profit
                    break
                
        return [ids, profit]