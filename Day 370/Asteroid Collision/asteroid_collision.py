class Solution:
    def asteroidCollision(self, N, asteroids):
        st = []
        for a in asteroids:
            while a < 0 and st and st[-1] > 0:
                pop = st.pop()
                
                if abs(a) == abs(pop):
                    a = 0
                elif abs(a) < abs(pop):
                    a = pop

            if a:
                st.append(a)
        return st