class Node:
    def __init__(self,data=None,next=None):
        self.data=data
        self.next=next
class Linkedlsit:
    def __init__(self):
        self.head=None
    
    def insert_at_start(self,data):
        node=Node(data,self.head)
        self.head=node
    
    def insert_at_end(self,data):
        node=Node(data)
        if self.head == None:
            self.head=node
        else:
            itr=self.head
            while itr.next != None:
                itr=itr.next
            itr.next=node

    def insert_anywhere(self,index,data):
        itr=self.head
        curr=self.head
        if index >= self.lenght_of_list():
            print("index out of range")
        else:
            for i in range(index-1):
                curr=curr.next
            for i in range(index):
                itr=itr.next
            node=Node(data,itr)
            curr.next=node
    
    def making_list_from_list(self,data_list):
        self.head=None
        for data in data_list:
            self.insert_at_end(data)

    def lenght_of_list(self):
        itr=self.head
        count=0
        while itr:
            itr=itr.next
            count+=1
        return count
    
    def getitem(self,index):
        if index >= self.lenght_of_list():
            print("index out of range")
        else:
            itr=self.head
            for i in range(index):
                itr=itr.next
            return itr.data

    def make_loop(self,index):
        itr=self.head
        prev=self.head
        for i in range(index):
            prev=prev.next
        while itr.next:
            itr=itr.next
        itr.next=prev.next

    def detect_loop(self):
        slow=self.head
        fast=self.head
        while slow and fast and fast.next:
            slow=slow.next
            fast=fast.next.next
            if slow == fast:
                return True
                break
        return False

    def printing(self):
        if self.head is None:
            print("LL is empty")
            return
        st=''
        if not self.detect_loop():
            itr=self.head
            while itr:
                if itr.next is not None:
                    st+=str(itr.data)+'-->'
                else:
                    st+=str(itr.data)
                itr=itr.next
        print(st)