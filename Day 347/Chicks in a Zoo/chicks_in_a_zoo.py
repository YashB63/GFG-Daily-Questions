class Solution:
	def NoOfChicks(self, N):
        lst = [1]
        for i in range(1, N):
            if i < 6:
                lst.append((sum(lst * 2)))
            else:
                lst.remove(lst[0])
                lst.append((sum(lst) * 2))
                
        return sum(lst)