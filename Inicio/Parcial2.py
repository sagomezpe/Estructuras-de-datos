from math import sqrt

#Define el nodo (llave y apuntador siguiente)
class Node:                         
    def __init__(self, data): 
        self.data = data
        self.ancho = 0
        self.largo = 0
        self.truck = 0
        self.next = None 
          
class LinkedList:

#Define apuntadores cabeza y cola    
    def __init__(self):              
        self.head = None
        self.tail = None 

#Devuelve lista enlazada        
    def isEmpty(self):               
        return self.head
    
    def getTruck(self,c):
        curr = self.head
        for i in range(1,c+1):
            lista = []
            while curr != None:
                if curr.truck == i:
                    lista.append(str(curr.data))
                curr = curr.next
            lista = " ".join(lista)    
            curr = self.head
            if i < c:
                print(str(i)+" "+lista)            
        print(str(i)+" "+lista, end="")
        
#Imprime lista    
    def print(self):                
        i = self.head
        while i != None:
            print("Nombre: " + str(i.data) + " Ancho: " + str(i.ancho) + 
                  " Largo: " + str(i.largo) + " Camion " +str(i.truck))
            i = i.next
        print()
        
    def package(self,id,x,y):
        node = Node(id)
        if self.head == None:
            self.head = node
            self.tail = node
            node.ancho = y
            node.largo = x
        else:
            self.tail.next = node
            self.tail = node
            node.ancho = y
            node.largo = x
                   
#Solo funciona cuando el numero de regiones tiene raiz entera
    def Region(self,ancho,largo,delta):
        count = 1
        anchoDelta = ancho/delta
        largoDelta = largo/delta
        largoTemp = largoDelta
        anchoTemp = anchoDelta
        
        #Si la lista esta vacia
        if self.head == None:
            node = Node(count)
            self.head = node
            self.tail = node
            node.ancho = anchoTemp
            node.largo = largoTemp
            largoTemp += largoDelta
            count += 1
            
        while anchoTemp <= ancho:
            while largoTemp <= largo:
                node = Node(count)
                self.tail.next = node
                self.tail = node
                node.ancho = anchoTemp
                node.largo = largoTemp
                largoTemp += largoDelta
                count +=1
            largoTemp = largoDelta
            anchoTemp += anchoDelta           

#Asigna el valor de la region
def Comparison(l1, l2):
    tempReg = l1
    tempPack = l2
    if tempReg == None:
        return
    if tempPack == None:
        return
    
    #Mientras que el ancho o el largo del paquete sea mayor 
    while (tempPack.ancho >= tempReg.ancho or tempPack.largo >= tempReg.largo) and tempReg.next != None:
        tempReg = tempReg.next  
    
    #Mientras que el nodo temporal no sea nulo 
    while tempPack.next != None:
        tempPack.truck = tempReg.data
        return Comparison(l1, tempPack.next)       
        
    if tempPack.next == None:
        tempPack.truck = tempReg.data
        return

#Geometria del taxista
def Manhattan(l1):
    temp = l1
    newList = LinkedList()
    newList.head = Node(0)
    newList.tail = Node(0)
    curr = newList.head
    prev = newList.head
    if temp == None:
        return 
    while temp != None:
        #Mientras la distancia es menor, se agrega despues del previo
        if (temp.ancho) < (curr.ancho) and curr.next != None:
            
            prev.next = Node(temp.data)
            prev.next.ancho = temp.ancho
            prev.next.largo = temp.largo
            prev.next.truck = temp.truck
            prev.next.next = curr
            
            temp = temp.next
            curr = newList.head
            prev = newList.head
            
        #Si la distancia es igual, se mira donde agreagar el nodo    
        elif (temp.ancho) == (curr.ancho) and (temp.ancho % 2) == 0 and curr.next != None:
            if (temp.largo < curr.largo):
                prev.next = Node(temp.data)
                prev.next.ancho = temp.ancho
                prev.next.largo = temp.largo
                prev.next.truck = temp.truck
                prev.next.next = curr
                    
                temp = temp.next
                curr = newList.head
                prev = newList.head
                    
            else:
                newTemp = curr.next
                curr.next = Node(temp.data)
                curr.next.ancho = temp.ancho
                curr.next.largo = temp.largo
                curr.next.truck = temp.truck
                curr.next.next = newTemp
                    
                temp = temp.next
                curr = newList.head
                prev = newList.head
            #Avanza hacia la izquierda        
        elif (temp.ancho) == (curr.ancho) and (temp.ancho % 2) == 0 and curr.next != None:
            if (temp.largo > curr.largo):
                prev.next = Node(temp.data)
                prev.next.ancho = temp.ancho
                prev.next.largo = temp.largo
                prev.next.truck = temp.truck
                prev.next.next = curr
                    
                temp = temp.next
                curr = newList.head
                prev = newList.head
                    
            else:
                newTemp = curr.next
                curr.next = Node(temp.data)
                curr.next.ancho = temp.ancho
                curr.next.largo = temp.largo
                curr.next.truck = temp.truck
                curr.next.next = newTemp
                    
                temp = temp.next
                curr = newList.head
                prev = newList.head
        
        #Si la distancia es mayor, se corre el nodo actual        
        elif (temp.ancho) > (curr.ancho) and curr.next != None:
            prev = curr
            curr = curr.next
                    
                
        #Si el nodo actual es la cola        
        elif curr.next == None:
            #Si es mayor que la cola, se agrega y se convierte en la nueva cola
            if (temp.ancho) > (curr.ancho):
                curr.next = Node(temp.data)
                curr.next.ancho = temp.ancho
                curr.next.largo = temp.largo
                curr.next.truck = temp.truck
                newList.tail = curr.next

                temp = temp.next
                curr = newList.head
                prev = newList.head
            #Si es igual que la cola, se mira el caso    
            elif (temp.ancho) == (curr.ancho) and temp.ancho % 2 == 0:
                #Avanza hacia la derecha
                if (temp.largo < curr.largo):
                    prev.next = Node(temp.data)
                    prev.next.ancho = temp.ancho
                    prev.next.largo = temp.largo
                    prev.next.truck = temp.truck
                    prev.next.next = curr
                        
                    temp = temp.next
                    curr = newList.head
                    prev = newList.head

                else: 
                    curr.next = Node(temp.data)
                    curr.next.ancho = temp.ancho
                    curr.next.largo = temp.largo
                    curr.next.truck = temp.truck
                    newList.tail = curr.next
                        
                    temp = temp.next
                    curr = newList.head
                    prev = newList.head
                       
            elif (temp.ancho) == (curr.ancho) and temp.ancho % 1 == 0:
                #Avanza hacia la izquierda 
                if (temp.largo > curr.largo):
                    prev.next = Node(temp.data)
                    prev.next.ancho = temp.ancho
                    prev.next.largo = temp.largo
                    prev.next.truck = temp.truck
                    prev.next.next = curr
                        
                    temp = temp.next
                    curr = newList.head
                    prev = newList.head

                else: 
                    curr.next = Node(temp.data)
                    curr.next.ancho = temp.ancho
                    curr.next.largo = temp.largo
                    curr.next.truck = temp.truck
                    newList.tail = curr.next
                        
                    temp = temp.next
                    curr = newList.head
                    prev = newList.head
            #Si es menor que la cola, se agrega despues de prev           
            else:
                prev.next = Node(temp.data)
                prev.next.ancho = temp.ancho
                prev.next.largo = temp.largo
                prev.next.truck = temp.truck
                prev.next.next = curr
                
                temp = temp.next
                curr = newList.head
                prev = newList.head

    #Se elimina la cabeza de comparacion        
    newList.head = newList.head.next                 
    return newList                 


entry1 = input()
entry1 = entry1.split(" ")
ancho = int(entry1[0])
largo = int(entry1[1])
regiones = int(entry1[2])
entry2 = input()
entry2 = entry2.split(" ")
paquetes = int(entry2[0])
montones = int(entry2[1])


delta = int(sqrt(regiones))
regionList = LinkedList()
regionList.Region(largo, ancho, delta)

#Bucles para anadir paquetes
packageList = LinkedList()
for _ in range(montones):
    paq = input()
    paq = paq.split()
    id = paq[0::3]
    x = paq[1::3]
    y = paq[2::3]
    i = 0
    for _ in range(len(id)):
        packageList.package(int(id[i]),int(x[i]),int(y[i]))
        i += 1
Comparison(regionList.head, packageList.head)
finalList = Manhattan(packageList.head)
finalList.getTruck(regiones)             


entry1 = input()
entry1 = entry1.split(" ")
ancho = int(entry1[0])
largo = int(entry1[1])
regiones = int(entry1[2])
entry2 = input()
entry2 = entry2.split(" ")
paquetes = int(entry2[0])
montones = int(entry2[1])


delta = int(sqrt(regiones))
regionList = LinkedList()
regionList.Region(largo, ancho, delta)

#Bucles para anadir paquetes
packageList = LinkedList()
for _ in range(montones):
    paq = input()
    paq = paq.split()
    id = paq[0::3]
    x = paq[1::3]
    y = paq[2::3]
    i = 0
    for _ in range(len(id)):
        packageList.package(int(id[i]),int(x[i]),int(y[i]))
        i += 1
Comparison(regionList.head, packageList.head)
finalList = Manhattan(packageList.head)
finalList.getTruck(regiones)