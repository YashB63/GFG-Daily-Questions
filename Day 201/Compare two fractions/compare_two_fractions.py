class Solution:
    def compareFrac (self, s):
        
        s = s.replace(","," ").replace("/"," ")
        arr = s.split()
        
        a = (arr[0])
        b = (arr[1])
        c = (arr[2])
        d = (arr[3])
        
        if int(a)/int(b) == int(c) / int(d) :
            return "equal"
        elif int(a)/int(b) < int(c)/int(d):
            return c+"/"+d
        else:
            return a+"/"+b