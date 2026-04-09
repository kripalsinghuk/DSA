class Priority:
    def __init__(self,val,priority):
        self.val = val
        self.priority = priority

class PriorityQueue:
    def __init__(self):
        self.myList = []
    def is_empty(self):
        length = len(self.myList)
        if length > 0:
            return False
        else:
            return True
    def push(self,val,priority):
        item = Priority(val,priority)
        if self.is_empty():
            self.myList.append(item)
        else:
            for index,value in enumerate(self.myList):
                if priority <= value.priority:
                    self.myList.insert(index,item)
                    break
            length = len(self.myList)-1
            if priority > self.myList[length].priority:
                self.myList.append(item)
    def printQueue(self):
        for i in self.myList:
            print("item",i.val,i.priority)
    def pop(self):
        if self.is_empty():
            raise Exception("empty queue")
        else:
            data = self.myList[0]
            self.myList.pop(0)
            return data
    def size(self):
        return len(self.myList)
p = PriorityQueue()
print(p.is_empty())
p.push(10,4)
p.push(30,3)
p.push(33,2)
p.push(343,30)
p.push(909,31)
p.push(2,1)
p.push(32,-1)
p.printQueue()
p.pop()
p.pop()
print("----------")
p.printQueue()
print(p.size())
