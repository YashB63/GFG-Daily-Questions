class Solution:
    def countSubs(self, s):
        
        class State:
            def __init__(self):
                self.length = 0
                self.link = -1
                self.next = {}
        
        n = len(s)
        st = [State() for _ in range(2 * n)]
        size = 1
        last = 0
        
        for ch in s:
            cur = size
            size += 1
            
            st[cur].length = st[last].length + 1
            
            p = last
            
            while p != -1 and ch not in st[p].next:
                st[p].next[ch] = cur
                p = st[p].link
            
            if p == -1:
                st[cur].link = 0
            else:
                q = st[p].next[ch]
                if st[p].length + 1 == st[q].length:
                    st[cur].link = q
                else:
                    clone = size
                    size += 1
                    
                    st[clone].length = st[p].length + 1
                    st[clone].next = st[q].next.copy()
                    st[clone].link = st[q].link
                    
                    while p != -1 and st[p].next.get(ch) == q:
                        st[p].next[ch] = clone
                        p = st[p].link
                    
                    st[q].link = clone
                    st[cur].link = clone
            
            last = cur
        
        ans = 0
        for i in range(1, size):
            ans += st[i].length - st[st[i].link].length
        
        return ans