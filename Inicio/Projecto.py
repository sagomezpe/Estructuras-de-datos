import time
from datetime import datetime

class LinkNode:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.next = None

class Node:
    def __init__(self, data): 
        self.data = data
        self.num = 0
        self.expenses = 0
        self.incomes = 0
        self.fecha = None     
        self.next = None

class TreeNode(object):
    def __init__(self, data):
        self.data = data
        self.num = 0
        self.expenses = 0
        self.incomes = 0
        self.left = None
        self.right = None
        self.height = 1
        
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
    def PushFront(self, user, key):
        nodo = LinkNode(user, key)
        if not self.isEmpty():
            self.head = nodo
            self.tail = nodo
        else:
            nodo.next = self.head
            self.head = nodo      

#Agrega elemento al final            
    def PushBack(self, user, key):
        nodo = LinkNode(user, key)
        if not self.isEmpty():
            self.head = nodo
            self.tail = nodo
        else:
            self.tail.next = nodo                
            self.tail = nodo

#Elimina elemento al inicio               
    def PopFront(self):
        curr = self.head
        cadena = (str(curr.username) + " " + str(curr.password))
        curr = curr.next
        self.head = curr
        return cadena        

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

#Crear usuario            
    def createUser(self, username, password):
        curr = self.head
        if curr == None:
            self.PushBack(username, password)
        while curr != None:
            if username == curr.username:
                print("El nombre de usuario ya esta registrado")
                return
            else: 
                curr = curr.next                
        self.PushBack(username, password)
        return print("El usuario ha sido creado")

#Buscar usuario            
    def searchUser(self, username, password):
        curr = self.head
        while curr != None:
            if username == curr.username:
                if password == curr.password:
                    print("Accediendo a la sesion")
                    return True
                else:
                    print("Clave incorrecta")
                    return False
            else:
                curr = curr.next  
        print("El usuario no existe")        
        return False                           
        
class Stack:
    def __init__(self):              
        self.head = None
        self.tail = None 
        
    def isEmpty(self):
        return self.head

    def push(self, data, num, expenses, incomes, fecha):
        nodo = Node(data)
        if not self.isEmpty():
            self.head = nodo
            self.tail = nodo
            self.head.num = num
            self.head.expenses = expenses
            self.head.incomes = incomes
            self.head.fecha = fecha             
        else:
            nodo.next = self.head
            self.head = nodo
            self.head.num = num
            self.head.expenses = expenses
            self.head.incomes = incomes
            self.head.fecha = fecha   

    def pop(self):
        curr = self.head
        cadena = (str(curr.data) + " " + str(curr.num) + " " + str(curr.expenses) + " " + str(curr.incomes) 
                  + " " + curr.fecha)
        curr = curr.next
        self.head = curr
        return cadena
        
    def print(self):
        curr = self.head
        while curr != None:
            print("Articulo: " + str(curr.data) + " Unidades: " + str(curr.num) + 
                  " Costos: " + str(curr.expenses) + " Ingresos:" + str(curr.incomes) 
                  + " Beneficios: " + str(curr.incomes - curr.expenses) + " Fecha de transaccion " 
                  + str(curr.fecha))
            curr = curr.next     
    
class Queue():
    def __init__(self):              
        self.head = None
        self.tail = None 
        
    def isEmpty(self):
        return self.head    
        
    def enqueue(self, data, num, expenses, incomes):
        nodo = Node(data)
        if not self.isEmpty():
            self.head = nodo
            self.tail = nodo
            self.head.num = num
            self.head.expenses = expenses
            self.head.incomes = incomes
             
        else:
            self.tail.next = nodo                
            self.tail = nodo
            self.tail.num = num
            self.tail.expenses = expenses
            self.tail.incomes = incomes

    def dequeue(self):
        curr = self.head
        cadena = (str(curr.data) + " " + str(curr.num) + " " + str(curr.expenses) + " " + str(curr.incomes))
        curr = curr.next
        self.head = curr
        return cadena
              
class AVLTree(object):

    def __init__(self):
        self.root = None 

    def insert(self, data, num, expenses, incomes):
        self.root = self.insert_node(self.root, data, num, expenses, incomes)

    def delete(self, data):
        self.root = self.delete_node(self.root, data)   

    def buy(self, data, num, price, stack):
        self._buy(self.root, data, num, price, stack)

    def sell(self, data, num, price, stack):
        self._sell(self.root, data, num, price, stack)

    # Function to insert a node
    def insert_node(self, root, data, num, expenses, incomes):

        # Find the correct location and insert the node
        temp = root
        if not root:
            root = TreeNode(data)
            root.num = num
            root.expenses = expenses
            root.incomes = incomes
            return root
        elif data < root.data:
            root.left = self.insert_node(root.left, data, num, expenses, incomes)
        elif data == root.data:
            root = temp
            print("Un articulo tiene el mismo nombre") 
            return root
        else:            
            root.right = self.insert_node(root.right, data, num, expenses, incomes)

        root.height = 1 + max(self.getHeight(root.left),
                              self.getHeight(root.right))

        # Update the balance factor and balance the tree
        balanceFactor = self.getBalance(root)
        if balanceFactor > 1:
            if data < root.left.data:
                return self.rightRotate(root)
            else:
                root.left = self.leftRotate(root.left)
                return self.rightRotate(root)

        if balanceFactor < -1:
            if data > root.right.data:
                return self.leftRotate(root)
            else:
                root.right = self.rightRotate(root.right)
                return self.leftRotate(root)

        return root
    
# Function to delete a node
    def delete_node(self, root, data):

        # Find the node to be deleted and remove it
        if not root:
            return root
        elif data < root.data:
            root.left = self.delete_node(root.left, data)
        elif data > root.data:
            root.right = self.delete_node(root.right, data)
        else:
            if root.left is None:
                temp = root.right
                root = None
                return temp
            elif root.right is None:
                temp = root.left
                root = None
                return temp
            temp = self.getMinValueNode(root.right)
            root.data = temp.data
            root.num = temp.num
            root.expenses = temp.expenses
            root.incomes = temp.incomes
            root.right = self.delete_node(root.right, temp.data)
        if root is None:
            return root

        # Update the balance factor of nodes
        root.height = 1 + max(self.getHeight(root.left),
                              self.getHeight(root.right))

        balanceFactor = self.getBalance(root)

        # Balance the tree
        if balanceFactor > 1:
            if self.getBalance(root.left) >= 0:
                return self.rightRotate(root)
            else:
                root.left = self.leftRotate(root.left)
                return self.rightRotate(root)
        if balanceFactor < -1:
            if self.getBalance(root.right) <= 0:
                return self.leftRotate(root)
            else:
                root.right = self.rightRotate(root.right)
                return self.leftRotate(root)
        return root
    
    
    def _buy(self, root, data, num, price, pila):
        
        if num <= 0:
            return print("El numero de elementos no es posible")
        
        if price <= 0:
            return print("El precio de compra no es posible")

        temp = self.root       
        if temp == None:
            return ("El elemento no existe")
        elif data == temp.data:
            temp.num = temp.num + num
            temp.expenses = temp.expenses + price
            now = datetime.now()
            pila.push(data, num, price, 0, now.strftime("%Y %m %d %H %M %S"))
            return
        elif data < temp.data:
            root = root.left
            self._buy(root, data, num, price, pila)        
        else:
            root = root.right            
            self._buy(root, data, num, price, pila)   
                     
        
    def _sell(self, root, data, num, price, pila):    
        if num <= 0:
            return print("El numero de elementos no es posible")
        if price <= 0:
            return print("El precio de venta no es posible")        
        temp = root       
        if temp == None:
            return ("El elemento no existe")
        elif data == temp.data:
            if temp.num-num < 0:
                return print("no hay suficientes unidades en el inventario, no se realiza la transaccion")
            else:
                temp.num = temp.num - num
                temp.incomes = temp.incomes + price
                now = datetime.now()
                pila.push(data, num, 0, price, now.strftime("%Y %m %d %H %M %S"))
                return   
        elif data < temp.data:
            root = root.left
            self._sell(root, data, num, price, pila)        
        else:
            root = root.right            
            self._sell(root, data, num, price, pila)  
        
    def search(self,root,data):
        temp = root
        if temp == None:
            return ("El elemento no existe")
        elif data == temp.data:
            return print("Nombre: " + str(temp.data) + " Inventario: " + str(temp.num) +
                    " Costo: " + str(temp.expenses) + " Ingreso: " + str(temp. incomes) + 
                    " Beneficios: " + str(temp.incomes-temp.expenses))  
        elif data < temp.data:
            temp = temp.left
            self.search(temp, data)        
        else:
            temp = temp.right            
            self.search(temp, data)     

                 
    def inOrder(self, root):
        if not root:
            return
        self.inOrder(root.left)
        print("Nombre: " + str(root.data) + " Inventario: " + str(root.num) + 
              " Costo: " + str(root.expenses) + " Ingresos:" + str(root.incomes) 
              + " Beneficios: " + str(root.incomes - root.expenses))
        self.inOrder(root.right)        
            

    # Function to perform left rotation
    def leftRotate(self, z):
        y = z.right
        T2 = y.left
        y.left = z
        z.right = T2
        z.height = 1 + max(self.getHeight(z.left),
                           self.getHeight(z.right))
        y.height = 1 + max(self.getHeight(y.left),
                           self.getHeight(y.right))
        return y

    # Function to perform right rotation
    def rightRotate(self, z):
        y = z.left
        T3 = y.right
        y.right = z
        z.left = T3
        z.height = 1 + max(self.getHeight(z.left),
                           self.getHeight(z.right))
        y.height = 1 + max(self.getHeight(y.left),
                           self.getHeight(y.right))
        return y

    # Get the height of the node
    def getHeight(self, root):
        if not root:
            return 0
        return root.height

    # Get balance factor of the node
    def getBalance(self, root):
        if not root:
            return 0
        return self.getHeight(root.left) - self.getHeight(root.right)

    def getMinValueNode(self, root):
        if root is None or root.left is None:
            return root
        return self.getMinValueNode(root.left)

    def saveQueue(self,root,cola):
        if not root:
            return
        self.saveQueue(root.left, cola)
        cola.enqueue(str(root.data), str(root.num), str(root.expenses), str(root.incomes))
        self.saveQueue(root.right, cola)

class HashMap():
    
    def __init__(self):
        self.size = 7
        self.map = [None] * self.size
    
    def _get_hash(self, key):
        hash = 0
        for char in str(key):
            hash += ord(char)
        return hash % self.size    
        
    def add(self, key, value):
        key_hash = self._get_hash(key)
        key_value = [key, value]
        
        if self.map[key_hash] is None:
            self.map[key_hash] = list([key_value])
            return True
        else:
            for pair in self.map[key_hash]:
                if pair[0] == key:
                    pair[1] = value
                    return True
            self.map[key_hash].append(key_value)
            return True          
        
    def get(self, key):
        key_hash = self._get_hash(key)
        if self.map[key_hash] is not None:
            for pair in self.map[key_hash]:
                if pair[0] == key:
                    return pair[1]
        return[None]        
        
    def delete(self, key):
        key_hash = self._get_hash(key)
        if self.map[key_hash] is None:
            return False
        for i in range(0, len(self.map[key_hash])):
            if self.map[key_hash][i][0] == key:
                self.map[key_hash].pop(i)
                return True 
        
    def print(self):
        for item in self.map:
            if item is not None:
                print(str(item))                
    
def checkFileExistance(filePath):

    try:
        with open(filePath, 'r') as f:
            return True
    except FileNotFoundError as e:
        return False
    except IOError as e:
        return False

def op1(link, queue, stack, tree):

    print("Bienvenido a su gestor de archivos, eliga una de las siguientes opciones")
    time.sleep(1)
    print("1 crear usuario")
    print("2 ingresar con su usuario")
    print("3 salir del programa")
    op = input()
    if op.isnumeric() == True:
        op = int(op)
        
        if op == 1:
            print("Inserte Nombre")
            username = input()
            print("Ingrese clave")
            password = input()
            link.createUser(username, password)
            op1(link, queue, stack, tree) 
                                              
        elif op == 2:
            print("Inserte Nombre")
            username = input()
            print("Ingrese clave")
            password = input()
            bool = link.searchUser(username, password)
            if bool == True:
                x2 = True
                
                #Fichero de articulos
                bool_art = checkFileExistance(str(username)+"_articulos.txt")
                if bool_art == True:
                    art = open(str(username)+"_articulos.txt", "r")
                else:     
                    art = open(str(username)+"_articulos.txt", "w")
                
                #Fichero de transacciones    
                bool_trans = checkFileExistance(str(username)+"_transacciones.txt")
                if bool_trans == True:
                    trans = open(str(username)+"_transacciones.txt", "r")
                else:     
                    trans = open(str(username)+"_transacciones.txt", "w")
                                
                for line in art:
                    x = line.split()
                    tree.insert(x[0],int(x[1]),float(x[2]),float(x[3]))
                
                for line in trans:    
                    x = line.split()
                    fecha_list = x[4:9]
                    fecha = " ".join(fecha_list)
                    stack.push(x[0],int(x[1]),float(x[2]),float(x[3]), fecha)
                
                art.close()
                trans.close()                
                op2(link, queue, stack, tree, username)
                                                       
        elif op == 3:
            return
            
        else:
            print("Ha ingresado una opcion incorrecta, intentelo de nuevo")
            time.sleep(2)
            op1(link, queue, stack, tree)
    
    else:
        print("No ha ingresado un numero, intentelo de nuevo")
        time.sleep(2)
        op1(link, queue, stack, tree)             

def op2(link, queue, stack, tree, username) :
    print("1 agregar elemento")
    print("2 eliminar elemento")
    print("3 comprar unidades")
    print("4 vender unidades")   
    print("5 buscar elemento")
    print("6 mostrar elementos")
    print("7 Ver transacciones historicas")
    print("8 Cerrar usuario")  
    print("Inserte operacion a realizar")
    op = input()
    if op.isnumeric() == True:
        op = int(op)
        
        #Agregar                
        if op == 1:
            print("Inserte Nombre")
            name = input()
            tree.insert(name, 0, 0, 0)
            op2(link, queue, stack, tree, username)      
        
        #Eliminar                                
        elif op == 2:
            print("Inserte Nombre")
            name = input()
            tree.delete(name, 0, 0, 0)
            op2(link, queue, stack, tree, username)
                
        #Comprar                    
        elif op == 3:
            print("Inserte Nombre")
            name = input()
            try:
                print("Inserte numero de elementos comprados") 
                sum = int(input())
                print("Inserte costo")
                price = float(input())
                tree.buy(name, sum, price, stack)
            except ValueError:
                print("Error, ha ingresado una cadena de caracteres")
                
            op2(link, queue, stack, tree, username)
                
        #Vender                    
        elif op == 4:
            print("Inserte Nombre")
            name = input()
            try:
                print("Inserte numero de elementos vendidos") 
                sum = int(input())
                print("Inserte ingreso")
                price = float(input())
                tree._sell(tree.root, name, sum, price, stack)
            except ValueError:
                print("Error, ha ingresado una cadena de caracteres")
                                      
            op2(link, queue, stack, tree, username)
        
        #Imprimir elemento                        
        elif op == 5:
            print("Inserte Nombre")
            name = input()
            tree.search(tree.root, name)        
            return op2(link, queue, stack, tree, username)
        
        #Imprimir elementos                        
        elif op == 6:
            tree.inOrder(tree.root)                
            return op2(link, queue, stack, tree, username)
                        
        #Historico de transacciones    
        elif op == 7:
            stack.print()
            return op2(link, queue, stack, tree, username)
        
        #Salir                    
        elif op == 8:
            print("Cerrando usuario")
            time.sleep(2)
            tree.saveQueue(tree.root, queue)
            art = open(str(username)+"_articulos.txt",'w')
            trans = open(str(username)+"_transacciones.txt",'w')
            
            #Se vacia la cola en el fichero
            while queue.head != None:
                item = queue.dequeue()
                art.write(item)
                art.write("\n")
            
            #Se vacia la pila en el fichero  
            while stack.head != None:
                tran = stack.pop()
                trans.write(tran)
                trans.write("\n")
                
            art.close()
            trans.close() 
            
            return op1(link, queue, stack, tree)
                                          
        else:
            print("Ha ingresado un valor erroneo, intentelo de nuevo")
            return op2(link, queue, stack, tree, username)
    else:
        print("No ha ingresado un numero")
        time.sleep(2)
        return op2(link, queue, stack, tree, username)

#Cargar objetos
hash = HashMap()
tree = AVLTree()
queue = Queue()
stack = Stack()
link = LinkedList()

#Abrir usuarios txt
bool_user = checkFileExistance("user.txt")
if bool_user == True:
    user = open("user.txt", "r")
else:     
    user = open("user.txt", "w+")

for line in user:
    x = line.split()
    link.PushFront(str(x[0]),str(x[1]))
user.close()

#Correr programa
op1(link, queue, stack, tree)    

#Guardar usuarios txt
user = open("user.txt", "w")        
while link.head != None:        
    user_name = link.PopFront()
    user.write(user_name)
    user.write("\n")
user.close()


print("Los datos se han guardado")
print("Programa finalizado") 