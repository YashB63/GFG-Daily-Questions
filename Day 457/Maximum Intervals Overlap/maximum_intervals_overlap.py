class Solution:
    def findMaxGuests(self, Entry, Exit, N):
        max_g = 0
        queue = []
        min_t = 0
        for _ in Entry:
            queue.append((_,1))
        for _ in Exit:
            queue.append((_,-1))
            
        queue.sort(key=lambda x:(x[0],-x[1]))
        
        n = len(queue)
        guest = 0
        for i in range(n):
            
            guest += queue[i][1]

            if  guest > max_g:
                max_g = guest
                min_t = queue[i][0]
            
        return (max_g, min_t)