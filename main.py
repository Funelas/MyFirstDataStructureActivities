class linkedlist:
    def __init__(self):
        self.head = None 
    def print_linkedlist(self):
        current_linkedlist = self.head # First to be accessed 
        while current_linkedlist != None:
            print(current_linkedlist.data)
            current_linkedlist = current_linkedlist.next
    
    def athead(self, newdata):
        NewNode = Node(newdata)
        NewNode.next = self.head 
        self.head = NewNode
            
    def atend(self, newdata):
        NewNode = Node(newdata)
        if self.head == None:
            self.head = NewNode
            return 
        current_node = self.head 
        while current_node.next != None:
            current_node = current_node.next 
        current_node.next = NewNode
    
    def insert_node(self, newelement, position):
        NewNode = Node(newelement)
        if position <= 0: # To show that position must only start at 1 
            print("\n Position should >= 1")
            if position == 0: 
                self.athead(newelement)
                return 
        else:
            temp = self.head
            previous_head = None 
            for _ in range(position):
                if temp.next != None:
                    previous_head = temp
                    temp = temp.next 
                else:
                    return print("Position out of order! Enter Valid Position")
            previous_head.next = NewNode
            NewNode.next = temp
class Node:
    def __init__(self, data = None):
        self.data = data 
        self.next = None 


list1 = linkedlist()
list1.head = Node ("Data")
e2 = Node("Structure")
e3 = Node("Python")

list1.head.next = e2 
e2.next = e3 

list1.athead("Welcome to")
list1.atend("Linked List")

list1.insert_node("the 2nd", 0)
list1.print_linkedlist()
