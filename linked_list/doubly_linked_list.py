class Node:
    def __init__(self,prev,val,next):
        self.prev = prev
        self.val = val
        self.next = next

class DoublyLinkedList:
    def __init__(self):
        self.head = None
    def insert(self,val):
        if self.head is None:
            self.head = Node(None,val,None)
        else:
            temp = self.head
            while temp.next is not None:
                temp = temp.next
            else:
                newNode = Node(temp,val,None)
                temp.next = newNode
    def printList(self):
         temp = self.head
         while temp.next is not None:
             print(temp.val)
             temp = temp.next
         else:
             print(temp.val)

    def insert_at_start(self,val):
        newNode = Node(None,val,self.head)
        self.head.prev = newNode
        self.head = newNode

    def insert_after_item(self,after_item,val):
        temp = self.head
        while temp.next is not None:
            if temp.val == after_item:
                newNode = Node(temp,val,temp.next)
                backup = temp
                temp.next = newNode
                backup.next.prev = newNode
                break
            temp = temp.next
        else:
            if temp.val == after_item:
                newNode = Node(temp,val,None)
                temp.next = newNode
            else:
                print("No element found after last")


    def insert_before_item(self,before_item,val):
        temp = self.head
        while temp.next is not None:
            if temp.val == before_item:
                newNode = Node(temp.prev,val,temp)
                backup = temp
                temp.prev.next =  newNode
                backup.prev = newNode
                break
            temp = temp.next
        else:
            if temp.val == before_item:
                newNode = Node(temp.prev,val,temp)
                backup = temp
                temp.prev.next = newNode
                backup.prev = newNode
            else:
                print("No element matched before last")

    def delete_from_last(self):
         temp = self.head
         while temp.next is not None:
             temp = temp.next
         else:
             backup = temp
             temp.prev = None
             backup.prev = None

d = DoublyLinkedList()
d.insert(10)
d.insert(20)
d.insert(30)
d.insert(40)
#d.printList()
d.insert_after_item(30,35)
d.insert_before_item(20,15)
#d.insert_after_item(33,32)
#d.insert_before_item(33,32)
d.printList()
d.delete_from_last()
d.printList() 
