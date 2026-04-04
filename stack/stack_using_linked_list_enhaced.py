class Node:
    def __init__(self,val,next):
        self.val = val
        self.next = next

class Stack:
    def __init__(self):
        self.head = None
        self.count = 0

    def is_empty(self):
        if self.head is None:
            return True
        else:
            return False

    def push(self,val):
        newNode=Node(val,self.head)
        self.head = newNode
        self.count=self.count+1

    def pop(self):
        data=self.head
        if self.head is not None:
             self.head = self.head.next
             self.count = self.count-1
             return data.val
        else:
            raise Exception("No eliment exsist.")

    def size(self):
        return self.count
    
    def peek(self):
        if self.head is not None:
            return self.head.val
        else:
            raise Exception("No eliment exsist.")
        
stack = Stack()
stack.push(10)
stack.push(30)
stack.push(40)
print(stack.size())
print(stack.is_empty())
print(stack.peek())
print(stack.pop())
print(stack.size())
