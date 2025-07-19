class Solution:
    def formCoils(self, n):
        m = 8*n*n
        coil1 = [0]*m
        coil1[0] = 8*n*n + 2*n
        curr = coil1[0]
        nflg = 1
        step = 2
        
        index = 1
        
        while index < m:
            for i in range(step):
                curr = curr - 4*n*nflg
                coil1[index] = curr
                index += 1
                if index >= m:
                    break
            
            if index >= m:
                break
            
            for i in range(step):
                curr = curr + nflg
                coil1[index] = curr
                index += 1
                if index >= m:
                    break
            
            nflg = (-nflg)
            step += 2
        
        coil2 = [0]*m
        i = 0
        
        for i in range(m):
            coil2[i] = 16*n*n + 1 - coil1[i]
        
        return [coil1,coil2]