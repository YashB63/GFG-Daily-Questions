class Solution:
    def enqueue(self, q, k):
        q.append(k)

    def findFrequency(self, q, k):
        frequency = 0
        for i in q:
            if i == k:
                frequency += 1
        return frequency