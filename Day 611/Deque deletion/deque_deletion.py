class Solution:
    def eraseAt(self, deq, x):
        ad = deque()
        for i in range(x):
            ad.append(deq.popleft())
        deq.popleft()
        while ad:
            deq.appendleft(ad.pop())

    def eraseInRange(self, deq, s, e):
        if s == e:
            return
        i = 0
        ad = deque()
        while i < s:
            ad.append(deq.popleft())
            i += 1
        while i < e:
            deq.popleft()
            i += 1
        while ad:
            deq.appendleft(ad.pop())

    def eraseAll(self, deq):
        deq.clear()
