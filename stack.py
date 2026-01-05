class Stack:

    def __init__(self):
        self.myList = []

    def push(self,item):
        self.myList.append(item)   
    def pop(self):
        self.myList.pop(-1)     
    def print(self):
        for l in self.myList:
            print(l)    


stack = Stack()
stack.push(2)
stack.push(4)
stack.push(7)
stack.print()
stack.pop()
stack.print()

