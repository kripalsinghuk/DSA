class Node:
    def __init__(self, item=None, next=None):
        self.item = item
        self.next = next


class SinglyLinkList:
    head = None
    last = Node()

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


s1 = SinglyLinkList()
s1.insert(10)
s1.insert(13)
s1.insert(14)
s1.insert(44)
s1.insert(55)
s1.insert(23)
s1.printList(s1)
