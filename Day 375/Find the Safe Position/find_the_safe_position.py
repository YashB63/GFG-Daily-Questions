class Solution:
    def safePos(self, n, k):
        people = list(range(1, n + 1))
        idx = 0
        return self.solve(people, k, idx)
        
    def solve(self, people, k, idx):
        if len(people) == 1:
            return people[0]
        
        idx = (idx + k - 1) % len(people)
        people.pop(idx)
        return self.solve(people, k, idx)