class Node(self,prev,val,next):
    def __init__(self,prev,val,next,pr):
        self.prev = prev
        self.val = val
        self.next = next
        self.pr = pr

class PriorityQueue:
    def __init__(self):
        self.head = None
        self.count = 0
    def size(self):
        return count
    def is_empty(self):
        if self.count>0:
            return False
        else:
            return True
    def push(self,val,pr):
        self.count+=1
        if self.head is None:
            newNode = Node(None,val,None,pr)
        else:
            temp = self.head
            while temp.next is not None:
                if pr < temp.pr:
                    newNode = Node(None,val,temp,pr)
                    temp
