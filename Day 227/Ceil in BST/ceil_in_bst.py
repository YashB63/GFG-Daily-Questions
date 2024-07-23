import math
class Solution:
    def findCeil(self,root, inp):
        if not root:return -1
        curr=root
        currentClosest=math.inf
        while curr:
            if curr.key==inp:
                currentClosest=curr.key
                break
            elif curr.key>inp:
                if curr.key<currentClosest:
                    currentClosest=curr.key
                curr=curr.left
            else:
                curr=curr.right
        return currentClosest if currentClosest!=math.inf else -1