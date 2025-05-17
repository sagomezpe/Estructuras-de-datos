import sys

class LinkNode:                         
    def __init__(self, key):
        self.key = key
        self.age = 0
        self.time = 0
        self.t = 0
        self.next = None

class TreeNode:
    def __init__(self, key):
        self.key = key
        self.age = 0
        self.time = 0
        self.t = 0
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
            print(str(i.key) + " " + str(i.age) + " " + str(i.time), end=" ")
            i = i.next
        print()

#Agrega elemento inicio       
    def PushFront(self, key, age, time, t):
        nodo = LinkNode(key)
        if not self.isEmpty():
            self.head = nodo
            self.tail = nodo
            self.head.age = age
            self.head.time = time
            self.head.t = t
        else:
            nodo.next = self.head
            self.head = nodo
            self.head.age = age
            self.head.time = time
            self.head.t = t
    
#Cuando el valor de t es t minimo (llega el primer cliente)    
    def data(self):
        temp = self.head
        nodo = self.head
        while temp != None:
            if int(nodo.time) > int(temp.time):
                nodo = temp
            else:
                temp = temp.next
        return nodo.key, nodo.age, nodo.time, nodo.t       
        
    def maxAge(self):
        temp = self.head
        nodo = self.head
        while temp != None:
            if int(nodo.age) < int(temp.age):
                nodo = temp
            else:
                temp = temp.next
        return nodo.key, nodo.age, nodo.time, nodo.t
        
class AVLTree:
    
    def __init__(self):
        self.root = None
        
    def insert(self, key, age, time, t):
        self.root = self.insert_node(self.root, key, age, time, t)
        
    def delete(self, key):
        self.root = self.delete_node(self.root, key)             

    def insert_node(self, root, key, age, time, t):
        if not root:
            root = TreeNode(key)
            root.age = age
            root.key = key
            root.time = time
            root.t = t
            return root
        elif key == root:
            return
        elif key < root.key:
            root.left = self.insert_node(root.left, key, age, time, t)
        else:
            root.right = self.insert_node(root.right, key, age, time, t)

        root.height = 1 + max(self.getHeight(root.left),self.getHeight(root.right))

        balanceFactor = self.getBalance(root)
        if balanceFactor > 1:
            if key < root.left.key:
                return self.rightRotate(root)
            else:
                root.left = self.leftRotate(root.left)
                return self.rightRotate(root)

        if balanceFactor < -1:
            if key > root.right.key:
                return self.leftRotate(root)
            else:
                root.right = self.rightRotate(root.right)
                return self.leftRotate(root)

        return root

    def delete_node(self, root, key):

        if not root:
            return root
        elif key < root.key:
            root.left = self.delete_node(root.left, key)
        elif key > root.key:
            root.right = self.delete_node(root.right, key)
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
            root.key = temp.key
            root.age = temp.age
            root.time = temp.time
            root.t = temp.t
            root.right = self.delete_node(root.right,temp.key)
        if root is None:
            return root
        
        root.height = 1 + max(self.getHeight(root.left),self.getHeight(root.right))
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
    
    #Busqueda
    def _searchMinTime(self, root, time, link):
        if not root:
            return
        if int(root.time) <= int(time):
            time = root.time
            link.PushFront(root.key, root.age, root.time, root.t)
        self._searchMinTime(root.left, time, link)
        self._searchMinTime(root.right, time, link)
    
    def _search(self, root, time, link):
        if not root:
            return
        if int(root.time) <= int(time):
            link.PushFront(root.key, root.age, root.time, root.t)
        self._search(root.left, time, link)
        self._search(root.right, time, link)
        
    def preOrder(self, root):
        if not root:
            return       
        self.preOrder(root.left)
        self.preOrder(root.right)    
    

tree = AVLTree()    
while True:
    li = input()
    if li == "FIN":
        break
    else:
        li = li.split()
        tree.insert(li[0], li[1], li[2], li[3])

time = 0
while tree.root != None:
    
    link = LinkedList()
    tree._searchMinTime(tree.root, 2000, link)
    list = link.data()
    minTime = list[2]
    key = list[0]
    t = list[3]
    
    if int(time) <= int(minTime):
        time = int(minTime) + int(t)
        tree.delete(key)
        print(key)
        
    else:
        link_1 = LinkedList()
        tree._search(tree.root, time, link_1)
        list_1 = link_1.maxAge()
        key = list_1[0]
        t = list_1[3]
        time = int(time) + int(t)
        tree.delete(key)
        print(key)
        
tree.preOrder(tree.root)