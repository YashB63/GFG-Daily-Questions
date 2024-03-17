class Solution:

    def transform(self, s):
        
        vow='AEIOUaeiou'
        
        ss=set(vow)
        
        for i in s:
            if i in ss:
                s=s.replace(i,'')
        if len(s)==0:
            return -1
        s1=''
        for i in s:
            s1+='#'+i.swapcase()
        return s1