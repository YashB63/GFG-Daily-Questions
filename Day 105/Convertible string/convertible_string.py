class Solution:
    def EqualString(self, s, t):
        
        if len(s)!=len(t):
            return 0
        elif s==t:
            return 1
            
        l1=[s[i] for i in range(len(s)) if i%2!=0]
        l2=[s[i] for i in range (len(s)) if i%2==0]
        l3=[t[i] for i in range (len(t)) if i%2!=0]
        l4=[t[i] for i in range (len(t)) if i%2==0]
        
        if sorted(l1)==sorted(l3) and sorted(l2)==sorted(l4):
            return 1

        return 0