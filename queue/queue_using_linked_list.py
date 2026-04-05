from linked_list.link_list import Node, SinglyLinkedList

class Queue(SinglyLinkedList):
    
    def __init__(self):
        super().__init__()
        self.count = 0
    
    def enqueue(self,val):
        self.insert_at_start(val)
        self.count = self.count+1
    
    def dequeue(self):
        try:
            super().delete_from_start()
            self.count = self.count-1
        except:
            print("Empty Queue")
    
    def size(self):
        return self.count
        
    def is_empty(self):
        if self.count > 0:
            return False
        else:
            return True

    def get_rear(self):
        if self.head is not None:
            return self.head.item
        else:
            raise IndexError("Empty Queue")

    def get_front(self):
       temp = self.head
       while temp.next is not None:
           temp = temp.next
       else:
           return temp.item
q1 = Queue()
q1.enqueue(10)
q1.enqueue(20)
q1.enqueue(30)
print(q1.size())
print(q1.is_empty())
print(q1.get_front())
print(q1.get_rear())
q1.dequeue()
print(q1.size())

