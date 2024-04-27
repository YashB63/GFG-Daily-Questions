class Solution:
    def common_element(self,v1,v2):
        
        dict = {}
        
        for i in v1:
            if i in dict.keys():
                dict[i] += 1
            else:
                dict[i] = 1
                
        list = []
                
        for i in v2:
            if i in dict.keys() and dict[i] > 0:
                list.append(i)
                dict[i] -= 1
                
        list.sort()
        
        return list