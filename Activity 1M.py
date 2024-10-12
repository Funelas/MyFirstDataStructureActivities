class linkedlist:
    def __init__(self):
        self.head = None 

    def printlist(self):
        printmoko = self.head 
        while printmoko is not None: 
            print(printmoko.data)
            printmoko = printmoko.next
    
    def athead(self, newdata):
        NewNode = Node(newdata)
        NewNode.next = self.head 
        self.head = NewNode 
    
    def atend(self, newdata):
        NewNode = Node(newdata)
        if self.head is None:
            self.head = NewNode  
            return
        lastnode = self.head 
        while (lastnode.next):
            lastnode = lastnode.next 
        lastnode.next = NewNode 

    def inpos (self, newelement, position):
        NewNode = Node(newelement)
        if (position <= 1):
            print("\n position should be >=1")
        elif (position == 1):
            NewNode.next = self.head 
            self.head = NewNode 
        else:
            temp = self.head 
            for i in range (1, position-1):
                if (temp != None):
                    temp = temp.next
            if (temp != None):
                NewNode.next = temp.next
                temp.next = NewNode
            else:
                print("List is null")
    def deleteNode(self, key):
        temp = self.head
        if temp is not None:
            if temp.data == key:
                self.head = temp.next 
                temp = None 
                return 
        while temp is not None:
            if temp.data == key:
                break 
            prev = temp 
            temp = temp.next 
        if temp == None:
            return 
        prev.next = temp.next
        temp = None
    def searchelement(self, searchValue):
        temp = self.head
        found = 0 
        i = 0
        if temp != None:
            while temp != None:
                i+=1
                if temp.data == searchValue:
                    found += 1
                    break 
                temp = temp.next 
            if found == 1:
                print(f"{searchValue} is found at index = {i}")
            else:
                print(f"{searchValue} is not found in the list.")
        else:
            print("The list is empty.")
class Node:
    def __init__(self, data = None):
        self.data = data
        self.next = None

list1 = linkedlist()
list1.head = Node("Data") # Example data for Module 3.1 Methods
s2 = Node("Structure") # Example data for Module 3.1 Methods
s3 = Node("Data") # Example data for Module 3.1 Methods
s4 = Node("Mining") # Example data for Module 3.1 Methods
s5 = Node("Data") # Example data for Module 3.1 Methods
s6 = Node("Cleaning") # Example data for Module 3.1 Methods
s7 = Node("Game") # Example data for Module 3.1 Methods
s8 = Node("Development") # Example data for Module 3.1 Methods

list1.head.next = s2 # Example data for Module 3.1 Methods
s2.next = s3 # Example data for Module 3.1 Methods
s3.next = s4 # Example data for Module 3.1 Methods
s4.next = s5 # Example data for Module 3.1 Methods
s5.next = s6 # Example data for Module 3.1 Methods
s6.next = s7 # Example data for Module 3.1 Methods
s7.next = s8 # Example data for Module 3.1 Methods

# list1.head = Node("Data") # Example data for Module 3 Methods
# e2 = Node("Structure")  # Example data for Module 3 Methods
# e3 = Node("Python")  # Example data for Module 3 Methods

# list1.head.next = e2 # Example data for Module 3 Methods
# e2.next = e3  # Example data for Module 3 Methods

# list1.athead("Welcome to") # For Inserting a data at the head of linked list
# list1.atend("Linked List") # For inserting a data at the end of linked list

# position = int(input("\n Where to insert Data, please indicate position number:")) # Start for inserting a data at a given position in the linked list
# data = "Stack"
# list1.inpos(data, position)
# list1.searchelement("Linked List") # End for inserting a data at a given position in the linked list

# a = input("Search: ") # Start for Searching a Node in the Linked List
# list1.searchelement(a) # End for searching a Node in the linked list


# list1.printlist() # Start For Deleting a Node in the Linked List
# a = input("\nEnter value you want to delete: ")
# list1.deleteNode(a)
# print("\nNew Linked List Content: ") # End For Deleting a Node in the Linked List


list1.printlist() # For Displaying the Linked List
