class Stack:
    #push,pop,is_empty,peek,size

    def __init__(self):
        self.myList = []
    def push(self,item):
        self.myList.append(item)   
    def pop(self):
        self.myList.pop(-1)  
    def peek(self):
        length = len(self.myList)
        if length == 0:
            raise ValueError("Empty list!")
        else:
            return self.myList[length-1]
    def is_empty(self):
        if len(self.myList) > 0:
            return False
        else:
            return True
    def size(self):
        return len(self.myList)    
    def print(self):
        for l in self.myList:
            print(l)    


stack = Stack()
print(stack.is_empty())
stack.push(2)
stack.push(4)
stack.push(7)
# stack.print()
# stack.pop()
stack.peek()
# stack.print()
print(stack.size())

