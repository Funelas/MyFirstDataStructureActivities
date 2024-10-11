class doublyLinkedList:
    def __init__(self):
        self.start_node = None 

    def InsertToEmptyList(self, data):
        if self.start_node is None:
            new_node = Node(data)
            self.start_node = new_node
        else:
            print("The list is not empty.")
    
    def InsertToEnd(self, data):
        # Check if the list is empty
        if self.start_node is None:
            new_node = Node(data)
            self.start_node = new_node
        n = self.start_node

        #Iterate until the next reaches None
        while n.next is not None:
            n = n.next
        new_node = Node(data)
        n.next = new_node
        new_node.prev = n
    
    def DeleteAtStart(self):
        if self.start_node is None:
            print(f"The Linked list is empty, no element to delete")
        elif self.start_node.next is None:
            self.start_node = None 
            return 
        self.start_node = self.start_node.next 
        self.start_prev = None
    
    def delete_at_end(self):
        # Check if the List is empty
        if self.start_node is None:
            print("The Linked list is empty, no element to delete")
        elif self.start_node.next is None:
            self.start_node = None 
            return 
        n = self.start_node
        while n.next is not None:
            n = n.next 
        n.prev.next = None 
    
    def Display(self):
        if self.start_node is None:
            print("The list is empty")
            return 
        else:
            n = self.start_node 
            while n is not None:
                print(f"Element is: ", n.item)
                n = n.next 
        print("\n")
    
class Node:
    def __init__(self, data):
        self.item = data 
        self.next = None 
        self.prev = None 

my_double_linkedlist = doublyLinkedList()
my_double_linkedlist.start_node = Node("Hello")

n2 = Node("world")
n3 = Node("John")
n4 = Node("Doe")
n5 = Node("i")
n6 = Node("lOvE")
n7 = Node("YOU")
n8 = Node("virus")

my_double_linkedlist.start_node.next = n2
n2.next, n3.next, n4.next, n5.next, n6.next, n7.next = n3,n4,n5,n6,n7,n8 
n2.prev, n3.prev, n4.prev, n5.prev, n6.prev, n7.prev, n8.prev = my_double_linkedlist.start_node, n2,n3,n4,n5,n6,n7

my_double_linkedlist.Display()


my_double_linkedlist.InsertToEnd("Ok Tayo?")
my_double_linkedlist.Display()