class Queue:
    def __init__(self):
        self.myList = []
    
    def is_empty(self):
        if len(self.myList)>0:
            return False
        else:
            return True
        
    def enqueue(self,val):
        self.myList.append(val)

    
    def dequeue(self):
        if self.is_empty():
            raise Exception("Empty Queue")
        else:
            self.myList.pop(0)
    
    def get_front(self):
        if self.is_empty():
            raise Exception("Empty Queue")
        else:
            return self.myList[0]
    
    def get_rear(self):
        if self.is_empty():
            raise Exception("Empty Queue")
        else:
            return self.myList[-1]

    def size(self):
        return len(self.myList)



queue = Queue()
queue.enqueue(1)
queue.enqueue(23)
queue.enqueue(233)
print(queue.size())
print(queue.is_empty())
print(queue.get_front())
print(queue.get_rear())
queue.dequeue()
print(queue.size())
print(queue.is_empty())
print(queue.get_front())
print(queue.get_rear())

