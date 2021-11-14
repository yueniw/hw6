#Question 5:

class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList(object):
    def __init__(self,head=None):
        self.head = head
    
    def insert(self, data):
        node = Node(data)
        current = self.head
        if not current:
            self.head = node
        else:
            while (current.next):
                current = current.next
            current.next = node
    
    def size(self):
        if self.head == None:
            return 0
        size = 0
        current = self.head
        while current:
            size += 1
            current = current.next
        return size
    
    def print_list(self):
        if self.head == None:
            raise ValueError("List is empty")
        current = self.head
        while current:
            print(current.data, end="  ")
            current = current.next

    def remove_dups(self):
        n = self.size()
        for i in range(n-1):
            curr=self.head
            nxt=curr.next
            prev=None
            while nxt:
                if curr.data>nxt.data:
                    if prev==None:
                        prev=curr.next
                        nxt=nxt.next
                        prev.next=curr
                        curr.next=nxt
                        self.head=prev
                    else:   
                        temp=nxt
                        nxt=nxt.next
                        prev.next=curr.next
                        prev=temp
                        temp.next=curr
                        curr.next=nxt
                else:           
                    prev=curr
                    curr=nxt
                    nxt=nxt.next
            i=i+1
        
        temp = self.head
        if temp is None:
            return
        while temp.next is not None:
            if temp.data == temp.next.data:
                new = temp.next.next
                temp.next = None
                temp.next = new
            else:
                temp = temp.next
        return self.head

#Test Cases:
linked_list = LinkedList(Node(11))
linked_list.insert(3)
linked_list.insert(6)
linked_list.insert(3)
linked_list.insert(11)
linked_list.insert(6)
linked_list.insert(5)
linked_list.insert(7)
linked_list.insert(5)
print("The Linked List is:")
linked_list.print_list()
linked_list.remove_dups()
print("After sorting, the Linked List is:")
linked_list.print_list()
