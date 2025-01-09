class Solution:
    def minLength(self, s, n): 
        st = []
        n = len(s)
        a = ["12","21","34","43","56","65","78","87","09","90"]
        for i in range(n):
            if st:
                ar = st[-1]+s[i]
                if ar in a:
                    st.pop()
                    continue
            st.append(s[i])
        return len(st)