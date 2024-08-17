class Solution:
    def __init__(self, id=0, deadline=0, profit=0):
        self.id = id
        self.deadline = deadline
        self.profit = profit
        
    def JobScheduling(self,Jobs,n):
        Jobs.sort(key=lambda x: x.profit, reverse=True)
        maxi = max(job.deadline for job in Jobs)
        slot = [-1] * (maxi + 1)
        countJobs = 0
        jobProfit = 0
        for i in range(n):
            for j in range(Jobs[i].deadline, 0, -1):
                if slot[j] == -1:
                    slot[j] = i
                    countJobs += 1
                    jobProfit += Jobs[i].profit
                    break
        return [countJobs, jobProfit]