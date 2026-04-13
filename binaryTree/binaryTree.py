class Node:
    def __init__(self,left,item,right):
        self.left = left
        self.item = item
        self.right = right
class Tree:
    def __init__(self):
        self.root = None
    def trev(self,temp):
        if temp is None:
            return
        print("trev",temp.item)
        if temp.left is None and temp.right is None:
            return
        if temp.left is None:
            self.trev(temp.right)
        elif temp.right is None:
            self.trev(temp.left)
        else:
            self.trev(temp.left)
            self.trev(temp.right)
    
    def callTrev(self):
        self.trev(self.root)
        
        
    def insert(self,item,temp):
        if temp is None:
            newNode = Node(None,item,None)
            self.root = newNode
            return
        if temp.left is None:
            temp.left = Node(None,item,None)
            return
        elif temp.right is None:
            temp.right = Node(None,item,None)
        else:
            self.insert(item,temp.left)
    
    def callInsert(self,item):
        self.insert(item,self.root)

t = Tree()
t.callInsert(2)
t.callInsert(3)
t.callInsert(4)
t.callInsert(5)
t.callTrev()
                
