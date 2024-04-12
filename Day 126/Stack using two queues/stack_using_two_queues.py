from queue import Queue   
   
def push(x):
    
    global queue_1
    global queue_2
    
    queue_1.put(x)

def pop():
    
    global queue_1
    global queue_2
    
    if queue_1.empty() and queue_2.empty():
        return -1
        
    if not queue_1.empty():
        while queue_1.qsize()>1:
            queue_2.put(queue_1.get())
            
        ans = queue_1.get()
        return ans
        
    else:
        while queue_2.qsize() > 1:
            queue_1.put(queue_2.get())
        ans = queue_2.get()
        return ans