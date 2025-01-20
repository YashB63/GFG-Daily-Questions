class Solution:
    def printMinNumberForPattern(ob,S): 
        res = []
        st = []
        n = len(S)
        for i in range(n+1):
            st.append(i+1)
            
            if i == n or S[i] == "I":
                while st:
                    res.append(st.pop())
        return "".join(map(str, res))