class Solution: 
    def minLaptops(self, n, start, end):
        start.sort()
        end.sort()
        i=1
        j=0
        total=1
        while i<n and j<n:
            if end[j]-start[i]>0:
                total+=1
            else:
                j+=1
            i+=1
        return total