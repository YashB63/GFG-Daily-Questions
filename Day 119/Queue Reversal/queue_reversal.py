class Solution:
    
    def rev(self, q):
        
        st=[]
        while not q.empty():
            x=q.get()
            st.append(x)
        while len(st)!=0:
            q.put(st.pop())
        return q