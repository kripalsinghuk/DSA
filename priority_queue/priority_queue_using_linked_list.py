class Node:
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
        return self.count
    def is_empty(self):
        if self.count>0:
            return False
        else:
            return True
    
    def push(self,val,pr):
        self.count+=1
        if self.head is None:
            newNode = Node(None,val,None,pr)
            self.head = newNode
        else:
            temp = self.head
            while temp.next is not None:
                if pr <= temp.pr:
                    newNode = Node(temp.prev,val,temp,pr)
                    if temp.prev is not None:
                        temp.prev.next = newNode
                        temp.prev = newNode
                    else:
                        self.head = newNode
                        temp.prev = newNode
                    break
                temp = temp.next
            else:
                if pr <= temp.pr:
                    newNode = Node(temp.prev,val,temp,pr)
                    if temp.prev is not None:
                        temp.prev.next = newNode
                        temp.prev = newNode
                    else:
                        self.head = newNode
                else:
                    newNode = Node(temp,val,None,pr)
                    temp.next = newNode
    def pop(self):
        if self.head is None:
            raise Exception("empty queue")
        else:
            temp = self.head
            self.head = self.head.next
            self.head.prev = None
            temp.next = None
            self.count-=1
            return temp.val

    def printQueue(self):
        temp = self.head
        if temp is None:
            raise Exception("Empty queue")
        while temp.next is not None:
            print("item",temp.val,temp.pr)
            temp = temp.next
        else:
            print("item",temp.val,temp.pr)

q = PriorityQueue()
q.push(10,4)
q.push(33,5)
q.push(89,0)
q.push(909,3)
q.push(89,2)
q.push(89,1)
q.push(3,92)
q.push(3,92)
q.push(3,93)
q.push(99,0)
q.push(100,1)
q.printQueue()
print(q.pop())
q.printQueue()
print(q.size())
print(q.is_empty())

