class Solution:
    def MedianOfArrays(self, array1, array2):
            
            x = array1 + array2
            x.sort()
            
            idx = len(x) // 2
            
            if(len(x) % 2 == 1):
                return int(x[idx])
                
            else:
                y = x[idx] + x[idx - 1]
                if(y % 2 == 0):
                    return y // 2
                else:
                    return y / 2