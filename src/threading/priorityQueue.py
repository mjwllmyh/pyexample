import Queue
import heapq 
import time

class PriorityQueue(Queue.Queue):
    # Initialize the queue representation
    def _init(self, maxsize):
        self.maxsize = maxsize
        self.queue = []

    # Put a new item in the queue
    def _put(self, item):
        return heapq.heappush(self.queue, item)

    # Get an item from the queue
    def _get(self):
        return heapq.heappop(self.queue)
    
    # wrap Queue's put and add priority argument
    def put(self, item, priority=0, block=True, timeout=None):
        decorated_item = priority, time.time(), item
        Queue.Queue.put(self, decorated_item, block, timeout)
        
    # wrap Queue's get and decorate
    def get(self,block=True,timeout=None):
        priority,time_posted,item=Queue.Queue.get(self, block, timeout)
        return item

if __name__ == "__main__":
    q = PriorityQueue()
    q.put((2,"a"))
    q.put((0,"b"))
    q.put((1,"c"))
    q.put((2,"d"))
    q.put((1,"e"))
    while not q.empty():
        print q.get()
