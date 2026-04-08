class Node:
    def __init__(self,prev,val,next):
        self.prev = prev
        self.val = val
        self.next = next
class Deck:
    def __init__(self):
        self.head = None
        self.count = 0
        self.front = None
        self.rear = None
    def is_empty(self):
        if self.count > 0:
            return False
        else:
            return True
    def insert_front(self,val):
        if self.head is None:
            self.head = Node(None,val,None)
            self.front = self.head
        else:
            newNode = Node(None,val,self.head)
            self.head.prev=newNode
            self.head = newNode
            self.front = newNode
        self.count+=1
    def insert_rear(self,val):
        temp = self.head
        self.count+=1
        while temp.next is not None:
            temp = temp.next
        else:
            newNode = Node(temp,val,None)
            temp.next = newNode
            self.rear = newNode
    def delete_front(self):
        if self.head.next is not None: 
            self.head.next.prev = None
            backup = self.head
            self.head = self.head.next
            backup.next = None
            self.front = self.head
        else:
            self.head = None
            self.front = self.head
        self.count-=1
    def delete_rear(self):
        temp = self.head
        while temp.next is not None:
            temp = temp.next
        else:
            self.rear = temp.prev
            temp.prev.next = None
            temp.prev = None
        self.count-=1
    def printDeck(self):
        temp = self.head
        while temp.next is not None:
            print(temp.val)
            temp = temp.next
        else:
            print(temp.val)
    def get_front(self):
        return self.front.val
    def get_rear(self):
        return self.rear.val
    def size(self):
        return self.count

deck = Deck()
deck.insert_front(10)
deck.insert_front(30)
deck.insert_rear(40)
deck.insert_rear(50)
deck.insert_rear(55)
deck.insert_front(5)
deck.printDeck()
print("-------")
deck.delete_front()
deck.delete_rear()
deck.printDeck()
print(deck.get_front())
print(deck.get_rear())
print(deck.size())
