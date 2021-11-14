class Node:
    def __init__(self, value=0):
        self.value = value
        self.prev = None
        
class ReversedLinkedList:
    def __init__(self, node):
        self.tail = Node(0)
        self.tail.prev = node
        
    def insert(self, val):
        tmp = self.tail.prev
        new_node = Node(val)
        self.tail.prev = new_node
        new_node.prev = tmp
    
    def delete(self, val):
        tmp_next = self.tail
        tmp = self.tail.prev
        while tmp != None:
            if (tmp.value == val):
                tmp_next.prev = tmp.prev
                return
            tmp_next = tmp
            tmp = tmp.prev
    
    def search(self, val):
        tmp = self.tail
        while tmp.prev != None:
            if (tmp.value == val):
                return True
            tmp = tmp.prev
        return False
    
    def print_list(self):
        tmp = self.tail
        while tmp.prev != None:
            tmp = tmp.prev
            print(str(tmp.value) + " ", end="")

#Test case
first_node = Node(11)
linked_list = ReversedLinkedList(first_node)
linked_list.insert(3)
linked_list.insert(6)
linked_list.insert(5)
print("The Linked List is (after insertion):")
linked_list.print_list()
linked_list.delete(6)
print("The Linked List is (after deleting 6):")
linked_list.print_list()
print("Does 5 exist in the Linked List?")
print(linked_list.search(5))
print("Does 17 exist in the Linked List?")
print(linked_list.search(17))