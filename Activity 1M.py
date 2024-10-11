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
list1.head = Node("Data")
s2 = Node("Structure")
s3 = Node("Data")
s4 = Node("Mining")
s5 = Node("Data")
s6 = Node("Cleaning")
s7 = Node("Game")
s8 = Node("Development")

list1.head.next = s2 
s2.next = s3 
s3.next = s4
s4.next = s5 
s5.next = s6 
s6.next = s7 
s7.next = s8 

list1.printlist()
a = input("Search: ")
list1.searchelement(a)


# Start of Module 3
# list1.head = Node("Data")
# e2 = Node("Structure")
# e3 = Node("Python")

# list1.head.next = e2
# e2.next = e3 

# list1.athead("Welcome to")
# list1.atend("Linked List")

# position = int(input("\n Where to insert Data, please indicate position number:"))
# data = "Stack"
# list1.inpos(data, position)
# list1.searchelement("Linked List")
# list1.printlist()
# End of Module 3

