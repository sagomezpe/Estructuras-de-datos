#Define el nodo (llave y apuntador siguiente)
class Node:                         
    def __init__(self, data): 
        self.data = data
        self.num = 0
        self.next = None 
        
class Stack:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def add(self, item):
        self.items.append(item)

    def get(self):
        return self.items.pop() 
    
class Queue:
    def __init__(self):
        self.head = None
        self.tail = None
        
    def isEmpty(self):
        return self.head    
        
    def enqueue(self, key):
        nodo = Node(key)
        if not self.isEmpty():
            self.head = nodo
            self.tail = nodo
        else:
            self.tail.next = nodo                
            self.tail = nodo
            
    def dequeue(self):
        curr = self.head
        curr = curr.next
        self.head = curr        
          
class LinkedList:

#Define apuntadores cabeza y cola    
    def __init__(self):              
        self.head = None
        self.tail = None 

#Devuelve lista enlazada        
    def isEmpty(self):               
        return self.head

#Imprime lista    
    def printList(self):                
        i = self.head
        while i != None:
            print(i.data, end=" ")
            i = i.next
        print()
        
    def delete(self, key):
        curr = self.head
        prev = None
        if curr == None:
            return
        if curr != None and curr.data == key:
            self.head = curr.next
            return self.delete(key);
        
        while curr!= self.tail:
            if curr.data != key:
                prev = curr
                curr = curr.next
            else: 
                curr = curr.next
                prev.next = curr
                return
        
        if curr == self.tail and curr == key:
            self.tail = prev
            self.tail.next = None        
                     
    def search(self,key):
        curr = self.head
        while curr:
            if curr.data == key:
                print(curr.data, curr.num)
                return
                
    def update(self,key,num):
        curr = self.head
        if curr == None:
            return print("El elemento no existe")            
        while curr:
            if curr.data == key:
                if num >= curr.num:
                    curr.num = curr.num + num
                    return               
        return print("la operacion no es posible")
        
                
#Agrega elemento teniendo en cuenta la unicidad               
    def add(self,key):
        nodo = Node(key)
        curr = self.head        
        if curr == None:
            self.head = Node(key)
            self.tail = Node(key)          
        self.tail.next = nodo
        print("La operacion se realizo con exito")                            
            
#Agrega elemento inicio       
    def PushFront(self, key):
        nodo = Node(key)
        if not self.isEmpty():
            self.head = nodo
            self.tail = nodo
        else:
            nodo.next = self.head
            self.head = nodo      

#Agrega elemento al final            
    def PushBack(self, key):
        nodo = Node(key)
        if not self.isEmpty():
            self.head = nodo
            self.tail = nodo
        else:
            self.tail.next = nodo                
            self.tail = nodo

#Elimina elemento al inicio               
    def PopFront(self):
        curr = self.head
        curr = curr.next
        self.head = curr        

#Elimina elemento al final                
    def PopBack(self):
        curr = self.head
        prev = None
        while curr != self.tail:
            prev = curr
            curr = curr.next
        if curr == self.tail:
            prev.next = None
            self.tail = prev
            
user = True
Li = LinkedList()
queue = Queue()
stack = Stack()
for i in range(10):
    Li.add("i")
Li.printList()    