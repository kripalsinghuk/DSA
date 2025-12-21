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
s1.insert(5)
# s1.insert(2)
# s1.insert(4)
# s1.insert(22)
# s1.insert(8)

s2.insert(1)
s2.insert(2)
s2.insert(4)
# s2.insert(303)
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
m = SinglyLinkList()

myList = Node()
firstNode = myList
while n1 is not None or n2 is not None:
    # if n1 is None and n2 is None:
    #     break
    if n1 is None:
        myList.next = n2
        break
    elif n2 is None:
        myList.next = n1
        break
    if n2.item>n1.item and n2.next<n1.item:
        if myList.item is None:     
            firstNode.item = n1.item  
            if n1.next.item<n2.item:     
                myList.item = n2.item
                firstNode.next = myList
            else:
                firstNode.next = myList   
        else:
            myList.next = Node(n1.item)
            myList.next.next= Node(n2.item)
    else:
        if myList.item is None:
            # print(n2.item)                 
            firstNode.item = n2.item 
            if n1.item<n2.next.item:     
                myList.item = n1.item
                firstNode.next = myList
            else:
                firstNode.next = myList   

        else:
            myList.next = Node(n2.item,Node(n1.item))
    if myList.next is not None:
        myList = myList.next.next
    n1 = n1.next
    n2 = n2.next

temp = firstNode    
while temp is not None:
    print(temp.item)
    temp = temp.next
       
