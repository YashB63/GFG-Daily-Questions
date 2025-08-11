class Solution:
    def makegraph(self, root, mp):
        q = deque()
        q.append(root)
        while q:
            it = q.popleft()
            if it.left:
                mp[it.left] = it
                q.append(it.left)
            if it.right:
                mp[it.right] = it
                q.append(it.right)
    
    def getNode(self, t, root):
        if not root:
            return None
        if root.data == t:
            return root
        left = self.getNode(t, root.left)
        if left:
            return left
        right = self.getNode(t, root.right)
        return right
    
    def sum_at_distK(self, root, target, k):
        mp = {}
        self.makegraph(root, mp)
        ans = 0
        targetNode = self.getNode(target, root)
        q = deque()
        q.append(targetNode)
        st = set()
        k += 1
        st.add(targetNode)
        while q and k:
            sz = len(q)
            while sz:
                it = q.popleft()
                ans += it.data
                if it.left and it.left not in st:
                    st.add(it.left)
                    q.append(it.left)
                if it.right and it.right not in st:
                    st.add(it.right)
                    q.append(it.right)
                if it in mp and mp[it] not in st:
                    st.add(mp[it])
                    q.append(mp[it])
                sz -= 1
            k -= 1
        return ans