class Solution:
    def isGoodorBad(self, S):
        vow,cons=0,0
        for i in S:
            if i in "aeiou":
                cons=0;vow+=1
            elif i=="?":
                vow+=1;cons+=1
            else:
                vow=0;cons+=1
            if vow>5 or cons>3:
                return 0
        return 1 