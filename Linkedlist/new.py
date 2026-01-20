class Node:
    def __init__(self,data):
        self.data=data 
        self.next=None

class singlelist:
    def __init__(self):
        self.head=None

    def add_at_head(self,data):
        new=Node(data)
        new.next=self.head
        self.head=new
        
    def add_at_tail(self,data):
        new=Node(data)
        if not self.head:
            self.head=new
            return
        temp=self.head
        while temp.next:
            temp=temp.next
        temp.next=new

    
