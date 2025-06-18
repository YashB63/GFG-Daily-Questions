class Solution:
    def findLength(self, color, radius):
        n = len(color)
        st = []

        for i in range(n):
            if st and color[i] == color[st[-1]] and radius[i] == radius[
                    st[-1]]:
                st.pop()
            else:
                st.append(i)

        return len(st)