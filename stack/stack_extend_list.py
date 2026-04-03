class Stack(list):
    # def __init__(self):
    #     # self.myList=[]
    #     pass

    def push(self, item):
        super().append(item)

    #it already exist in parent class so why create it.
    # def pop(self): 
    #     super().pop()

    def peek(self):
        length = len(self)
        if length == 0:
            raise Exception("Empty List!")
        else:
            return self[length - 1]

    def size(self):
        return len(self)

    def is_empty(self):
        if len(self) > 0:
            False
        else:
            True

    def append(self, item):
        raise Exception("This method is not allowed!")



stack = Stack()
stack.push(1)
stack.push(2)
stack.push(3)
stack.pop()
stack.is_empty()
stack.size()
# stack.append(2)
