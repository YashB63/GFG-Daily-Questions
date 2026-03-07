class Solution:
    def areIsomorphic(self, s1, s2):
        if len(s1) != len(s2):
            return False
            
        map_s1 = {}
        map_s2 = {}
        n= len(s1)
        for i  in range (n):
            
            ch1  = s1[i]
            ch2  = s2[i]
            
            if ch1 in map_s1:
                if map_s1[ch1] != ch2:
                    return False
                    
            else:
                map_s1[ch1] = ch2
                
                
            if ch2 in map_s2:
                if map_s2[ch2] != ch1:
                    return False
                    
            else:
                map_s2[ch2] = ch1
                
        return True