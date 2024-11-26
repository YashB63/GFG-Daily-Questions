class Solution:
	def follPatt(self, s):
        n = len(s)
        xCount = 0
        yCount = 0
    
        for i in range(n):
            if s[i] == 'x':
                if yCount > 0:
                    if xCount != yCount:
                        print(0)
                        return  
                    xCount = 0
                    yCount = 0
                xCount += 1
            elif s[i] == 'y':
                if xCount == 0:
                    print(0)
                    return  
                yCount += 1
    
        if xCount == yCount:
            print(1)
        else:
            print(0)