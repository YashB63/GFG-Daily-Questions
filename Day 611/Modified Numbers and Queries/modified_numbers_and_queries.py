query = [0] * (10001)
flag = False

def pre():

    query[1] = 0
    for i in range(2, 10001):
        if query[i] == 0:
            for j in range(2 * i, 10001, i):
                query[
                    j] += i  
    query[2] = 2
    for i in range(3, 10001, 2):
        if query[i] == 0:
            query[
                i] = i  
    for i in range(2, 10001):
        query[i] += query[i - 1]


class Solution:

    def sumOfAll(self, l, r):
        global flag
        if not flag:  
            pre()
            flag = True  

        return query[r] - query[l - 1]