class Solution:
	def overlappedInterval(self, Intervals):
        Intervals.sort(key=lambda x:x[0])
        index = 0
        for i in range(1,len(Intervals)):
            if(Intervals[index][1]>=Intervals[i][0]):
                Intervals[index][1] = max(Intervals[index][1],Intervals[i][1])
            else:
                index+=1
                Intervals[index] = Intervals[i]
        
        return Intervals[0:index+1]