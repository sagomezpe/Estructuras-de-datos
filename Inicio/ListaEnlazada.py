#Define el nodo (llave y apuntador siguiente)
class Node:                         
    def __init__(self, data): 
        self.data = data
        self.next = None 


          
class LinkedList:

#Define apuntadores cabeza y cola    
    def __init__(self):              
        self.head = None
        self.tail = None 

#Devuelve lista enlazada        
    def isEmpty(self):               
        return self.head

#Imprime lista    
    def print(self):                
        i = self.head
        while i != None:
            print(i.data, end=" ")
            i = i.next
        print()

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
            
#Elimina elementos repetidos
    def DelRep(self):
        curr = self.head    
        prev = None
        duplicate = dict()
        while curr:
            if curr.data not in duplicate:
                duplicate[curr.data] = None
                prev = curr
            else:
                prev.next = curr.next
                curr = curr.next
                
class Solution:
    def mergeTwoLists(self, l1: LinkedList, l2: LinkedList) -> LinkedList:
        if l1 is None:
            return l2
        
        if l2 is None:
            return l1


        newHead = LinkedList(-1)
        cur = newHead
        while l1 and l2:
            if l1.val >= l2.val:
                cur.next = l2
                l2 = l2.next
            else:
                cur.next = l1
                l1 = l1.next
            # Cuando cur.next no es None, debe mover el puntero cur al mismo tiempo
            cur = cur.next
            
        if l1:
            cur.next = l1
            return newHead.next
        
        if l2:
            cur.next = l2
            return newHead.next                     

            
            
if __name__ == '__main__':
    listA = LinkedList()
    listB = LinkedList()
    merged_list = LinkedList()
    t = input()
    n = int(input())
    for _ in range(n):
        listA.PushBack(input())
    m = int(input())
    for i in range(m):
        listB.PushBack(input())
    listA.print()
    listB.print()
    Solution.mergeTwoLists(merged_list,listA,listB)


                
    