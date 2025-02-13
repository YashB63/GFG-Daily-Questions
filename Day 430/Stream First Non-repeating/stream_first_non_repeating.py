from collections import deque

class Solution:
	def FirstNonRepeating(self, s):
        length=len(s)
        count ={}
        q=deque()
        st=""
        
        for ch in s:
            if ch in count:
                count[ch]+=1
            else:
                count[ch]=1
                
            q.append(ch)
            
            while q and count[q[0]]>1:
                q.popleft()
              
            st+=q[0] if q else '#'
          
        return st