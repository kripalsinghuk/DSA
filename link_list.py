class Node:
    def __init__(self, item=None, next=None):
        self.item = item
        self.next = next


class SinglyLinkList:
    # head = None
    # last = Node()
    def __init__(self,head=None,last=None):
        self.head = head
        self.last = Node()

    def insert(self, item):
        node = Node()
        node.item = item
        if self.head == None:
            self.head = node
        else:
            self.last.next = node
        self.last = node

    def printList(self, list):
        n = list.head
        while n.next != None:
            print(n.item)
            n = n.next
            if(n.next == None):
                print(n.item)
    def deleteFirst(self,list):
        list.head = list.head.next



s1 = SinglyLinkList()
s2 = SinglyLinkList()
s1.insert(1)
s1.insert(3)
s1.insert(4)
s1.insert(22)
# s1.insert(8)

s2.insert(1)
s2.insert(2)
s2.insert(5)
# s2.insert(5)
# s1.insert(55)
# s1.insert(23)
# s1.printList(s1)
# s1.deleteFirst(s1)
# s1.printList(s1)
# print('---')
# s2.printList(s2)

n1 = s1.head
n2 = s2.head
while n1 is not None and n2 is not None:
    # print(n1.item,n2.item)
    if n2.item>=n1.item:
        newNode = Node(n2.item,n1.next)
        n1.next = newNode
        n1 = n1.next.next
    else:
        # print(n1.item)
        newNode = Node(n2.item,n1)
    # n1 = n1.next.next
    n2 = n2.next
temp = s1.head    
while temp is not None:
    print(temp.item)
    temp = temp.next    
