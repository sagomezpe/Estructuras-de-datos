import time
from datetime import datetime
from tkinter import messagebox

#Nodo usuario
class LinkNode:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

class Node:
    def __init__(self, data): 
        self.data = data
        self.num = 0
        self.expenses = 0
        self.incomes = 0
        self.fecha = None     
        self.next = None

#Nodo articulo
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
        cadena = (str(curr.key) + " " + str(curr.value))
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
                return False
            else: 
                curr = curr.next                
        self.PushBack(username, password)
        return True

#Buscar usuario            
    def searchUser(self, username, password):
        curr = self.head
        while curr != None:
            if username == curr.username:
                if password == curr.password:
                    return 0
                else:
                    return 1
            else:
                curr = curr.next       
        return 2                          
        
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
        
    def search(self, data):
        self._search(self.root, data)
        
    def inOrder(self):
        self._inOrder(self.root)        

    def insert_node(self, root, data, num, expenses, incomes):
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
            messagebox.showerror("Error","Un articulo tiene el mismo nombre") 
            return root
        else:            
            root.right = self.insert_node(root.right, data, num, expenses, incomes)

        root.height = 1 + max(self.getHeight(root.left),
                              self.getHeight(root.right))

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
    
    def delete_node(self, root, data):
        if not root:
            return root
        elif data < root.data:
            root.left = self.delete_node(root.left, data)
        elif data > root.data:
            root.right = self.delete_node(root.right, data)
        else:
            if root.num > 0:
                messagebox.showerror("Error","No se puede borrar el elemento debido a que existe inventario")
                return self.root
            elif root.left is None:
                temp = root.right
                root = None
                messagebox.showinfo("","El elemento ha sido eliminado con exito")
                return temp
            elif root.right is None:
                temp = root.left
                root = None
                messagebox.showinfo("","El elemento ha sido eliminado con exito")
                return temp
            temp = self.getMinValueNode(root.right)
            root.data = temp.data
            root.num = temp.num
            root.expenses = temp.expenses
            root.incomes = temp.incomes
            root.right = self.delete_node(root.right, temp.data)
        if root is None:
            return root

        root.height = 1 + max(self.getHeight(root.left),
                              self.getHeight(root.right))

        balanceFactor = self.getBalance(root)

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
        
               
        if root == None:
            messagebox.showinfo("","El elemento no existe")
            return 
        elif data == root.data:
            root.num = root.num + num
            root.expenses = root.expenses + price
            now = datetime.now()
            pila.push(data, num, price, 0, now.strftime("%Y %m %d %H %M %S"))
            messagebox.showinfo("", "La transaccion se ha realizado con exito")
            return
        elif data < root.data:
            self._buy(root.left, data, num, price, pila)        
        else:           
            self._buy(root.right, data, num, price, pila)   
                             
    def _sell(self, root, data, num, price, pila):    
        
        if root == None:
            messagebox.showinfo("","El elemento no existe")
            return 
        
        elif data == root.data:
            if root.num-num < 0:
                messagebox.showinfo("","No hay suficientes unidades en el inventario, no se realiza la transaccion")
                return
            else:
                root.num = root.num - num
                root.incomes = root.incomes + price
                now = datetime.now()
                pila.push(data, num, 0, price, now.strftime("%Y %m %d %H %M %S"))
                messagebox.showinfo("", "La transaccion se ha realizado con exito")
                return   
        elif data < root.data:
            self._sell(root.left, data, num, price, pila)        
        else:           
            self._sell(root.right, data, num, price, pila)  
        
    def _search(self,root,data):
        if root == None:
            return messagebox.showerror("Error","El elemento no existe")
        elif data == root.data:
            return messagebox.showinfo("Elemento encontrado","Nombre: " + str(root.data) + " Inventario: " + str(root.num) +
                    " Costo: " + str(root.expenses) + " Ingreso: " + str(root. incomes) + 
                    " Beneficios: " + str(root.incomes-root.expenses))  
        elif data < root.data:
            self._search(root.left, data)        
        else:          
            self._search(root.right, data)     
             
    def _inOrder(self, root):
        if not root:
            return
        self._inOrder(root.left)
        print("Nombre: " + str(root.data) + " Inventario: " + str(root.num) + 
              " Costo: " + str(root.expenses) + " Ingresos:" + str(root.incomes) 
              + " Beneficios: " + str(root.incomes - root.expenses))
        self._inOrder(root.right)        
            
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

    def getHeight(self, root):
        if not root:
            return 0
        return root.height

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

class HashTable:
    def __init__(self):
        self.cap = 103
        self.size = 0
        self.x = 3
        self.linked = [None] * self.cap

    def hash(self,key):
        hash = 0
        count = 0
        for letter in key:
            hash += (ord(letter)*pow(self.x, count))
            count += 1
        hash = hash % self.cap    
        return hash
        
    def insert(self, key, value):
        self.size += 1
        index = self.hash(key)
        node = self.linked[index]
        if node == None:
            self.linked[index] = LinkNode(key,value)
            return True
        else:
            temp = node
            while node != None:
                if key == node.key:
                    return False
                else:
                    temp = node
                    node = node.next
            temp.next = LinkNode(key,value)
            return True
        
    def search(self, key, value):
        index = self.hash(key)
        node = self.linked[index]
        while node != None and node.key != key:
            node = node.next
        if node == None:
            return 2
        else:
            if node.value == value:
                return 0
            else:
                return 1
    
    def save(self, link):
        for i in range(self.cap):
            node = self.linked[i]
            while node != None:
                link.PushBack(node.key, node.value)
                node = node.next