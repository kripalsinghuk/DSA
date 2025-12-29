class DLL:
    def __init__(self,head=None):
        self.head = head
        
    def insert_at_start(self,val):
        if self.head==None:
            self.head = ListNode(None,val,None)
        else:
            self.head = ListNode(None,val,self.head)
            
    def insert_at_last(self,val):
        if self.head==None:
            self.head = ListNode(None,val,None)
        else:
            temp = self.head
            while temp is not None:
                if temp.nxt is None:
                    temp.nxt = ListNode(temp,val,None)
                    break
                temp = temp.nxt
    
    def delete_item(self,val):
        temp = self.head
        if self.head==None:
            print('List is empty')
        while temp is not None:
            if temp.val == val:
                if temp.prev == None:
                    head = temp.nxt
                    print("it was start node, deleted succesfully")
                    break
                elif temp.nxt is None:
                    lastNode = temp.prev
                    temp.prev = None
                    lastNode.nxt = None
                    print("it was last Node deleted succesfully")
                    break
                else:
                    prevNode = temp.prev
                    nxtNode = temp.nxt
                    prevNode.nxt = nxtNode
                    nxtNode.prev = prevNode
                    print("it was middle node deleted successfullyt")
                    break
            temp = temp.nxt    
        else:
            print('element not found.')
            
    def printList(self):
        if self.head==None:
            print('empty')
        else:
            temp = self.head
            while temp is not None:
                print(temp.val)
                temp = temp.nxt
        
class ListNode:
    def __init__(self,prev=None,val=None,nxt=None):
        self.prev = prev
        self.val = val
        self.nxt = nxt
list1 = DLL()
list1.printList()
list1.insert_at_start(20)
list1.insert_at_start(10)
list1.insert_at_last(30)
list1.insert_at_last(40)
list1.insert_at_last(50)
list1.insert_at_last(60)
list1.insert_at_start(0)
list1.printList()
list1.delete_item(0)
list1.delete_item(30)
list1.delete_item(60)
list1.printList()