class Node:
    def __init__(self,val,nxt):
        self.val = val
        self.nxt = nxt
class SLL:
    def __init__(self):
        self.head = None

    def insert_at_start(self,val):
        if self.head is None:
            self.head = Node(val,None)
        else:
            self.head =  Node(val,self.head)

    def delete_at_start(self):
        if self.head.nxt is not None:
            self.head = self.head.nxt
   
    def is_empty(self):
        if self.head is None:
            return True
        else:
            return False

    def size(self):
        if self.head is None:
            return 0

        temp = self.head
        count=0
        while temp.nxt is None:
            count=count+1
            temp=temp.nxt
        else:
            count=count+1
        return count    

    def show(self):
        temp = self.head
        while temp.nxt is not None:
            print(temp.val)
            temp = temp.nxt
        else:
            print(temp.val)

class Stack:
    def __init__(self):
        self.sll = SLL()
    def push(self,item):
        self.sll.insert_at_start(item)
    def pop(self):
        self.sll.delete_at_start()
    def show(self):
        self.sll.show()
    def is_empty(self):
        return self.sll.is_empty()
    def size(self):
        return self.sll.size()


stack = Stack()
print(stack.is_empty())
print(stack.size())
stack.push(1)
stack.push(2)
stack.push(3)
stack.show()   
stack.pop()
stack.show()
print(stack.is_empty())
print(stack.size())
