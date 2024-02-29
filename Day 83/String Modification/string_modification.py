from heapq import *

class Solution:
   
    def rearrangeString(self, string):
       
        n = len(string)
        count = [0]*26
        for i in range(n):
            count[ord(string[i]) - 97] += 1
            
        pq = []
        res = ''
        for i in range(97, 123):
            if count[i - 97] != 0:
                heappush(pq, [-1*count[i-97], chr(i)])
                
        prev = [1, '#']
        while pq!= []:
            ky = heappop(pq)
            res = res + ky[1]
            if prev[0] < 0:
                heappush(pq, prev)
            ky[0] += 1
            prev = ky
            
        if len(res) != n:
            return '-1'
            
        return res