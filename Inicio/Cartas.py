#Define el nodo (llave y apuntador siguiente)
class Node:                         
    def __init__(self, data):
        self.score = 0
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
        
#Obtener puntajes de la lista
    def getScore(self):
        i = self.head
        x = []
        while i != None:
            x.append(i.score)
            i = i.next
        return x

#Obtener ganadores    
    def getWinners(self):
        i = self.head
        temp = -1
        x = []
        while i != None:
            if i.score > temp:
                temp = i.score
            i = i.next
        i = self.head    
        while i != None:
            if i.score == temp:
                x.append(str(i.data))
            i = i.next
        return x        
                
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
        if self.head == self.tail:
            self.head = None
            self.tail = None
            return
        curr = self.head
        curr = curr.next
        self.head = curr


#Elimina elemento al final                
    def PopBack(self):
        curr = self.head
        prev = None
        if self.head == self.tail:
            self.head = None
            self.tail = None
            return
        while curr != self.tail:
            prev = curr
            curr = curr.next
        if curr == self.tail:
            prev.next = None
            self.tail = prev

#Compara las cartas con los jugadores y asigna los valores            
def Assign(l1, l2):
    #nodo para operar:
    temp = l2.head
    #Condiciones para una lista vacia
    if l1.head == None:
        return
    if l2.head == None:
        return
    #Mientras existan cartas
    while l1.head != None:
        #Si se encuentra jugador, sus valores
        if temp != None:
            first = l1.head.data
            last = l1.tail.data
            if first >= last:
                l1.PopFront()
                temp.score += first
                temp = temp.next
            else:
                l1.PopBack()
                temp.score += last
                temp = temp.next

    #Si recorre la lista de jugadores, vuelve al inicio    
        if temp == None:
            temp = l2.head
        
    
casos = int(input())
for t in range(casos):
    x = []
    liCartas = LinkedList()
    liJugadores = LinkedList()
    prueba = input()
    prueba = prueba.split()
    N = int(prueba[0])
    K = int(prueba[1])
    cartas = input()
    cartas = cartas.split()
    #Se crea un nodo para cada jugador
    for i in range(1,K+1):
        liJugadores.PushBack(int(i))
    #Se crea un nodo para cada carta
    for j in cartas:
        liCartas.PushBack(int(j))  
    #Metodo que asigna el puntaje de las cartas
    Assign(liCartas, liJugadores)
    #Asigna el numero de los ganadores a una lista
    x = liJugadores.getWinners()
    y = " ".join(x)
    print("Caso #" + str(t+1) +":")
    print(y)