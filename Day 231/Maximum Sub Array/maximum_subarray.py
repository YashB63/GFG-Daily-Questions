import sys

class Solution:
	def findSubarray(self,n, a):
        maxi = -sys.maxsize - 1  
        sum = 0

        start = 0
        ansStart, ansEnd = -1, -1
        for i in range(n):
            if sum == 0 and a[i] >= 0:
                start = i  
            if a[i] >= 0:
                sum += a[i]
            else:
                sum = 0

            if sum > maxi or (sum == maxi and (i - start > ansEnd - ansStart)):
                maxi = sum
                ansStart = start
                ansEnd = i

            if sum < 0:
                sum = 0

        if ansStart == -1:
            return [-1]
        return a[ansStart:ansEnd+1]