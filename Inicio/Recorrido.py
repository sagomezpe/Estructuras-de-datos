import sys

class TreeNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.height = 1

class AVLTree:
    
    def __init__(self):
        self.root = None
        
    def insert(self,key):
        self.root = self.insert_node(self.root, key)
        
    def delete(self,key):
        self.root = self.delete_node(self.root, key)             

    def insert_node(self, root, key):

        if not root:
            return TreeNode(key)
        elif key == root:
            return
        elif key < root.key:
            root.left = self.insert_node(root.left, key)
        else:
            root.right = self.insert_node(root.right, key)

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
    
    def path(self,start,end):
        if not self.root:
            return
        elif start == self.root.key:
            print(str(self.root.key) + "," , end="")
            self._depth(self.root,end)
        else:    
            self._path(self.root, start, end, self.root)

    def _path(self, root, start, end, temp):
        #temp es el nodo padre
        
        if start == root.key:
            
            print(str(root.key) + "," , end="")
            
            #Si es mayor que todos los nodos en el subarbol
            
            if end == temp.key:
                print(str(temp.key), end="")
                return
            
            elif temp.key == self.root.key:
                print(str(temp.key) + "," , end="")
                self._depth(self.root, end)
            
            #Arreglar
            elif end > temp.key and end > root.key:
                if root.key < temp.key:
                    print(root.key)
                    self._depth(root,end)
                else:    
                    start = temp.key
                    self._path(self.root, start, end, self.root)
                    
            elif end < temp.key and end < root.key:
                if root.key < temp.key:
                    self._depth(root,end)
                else:    
                    start = temp.key
                    self._path(self.root, start, end, self.root)                
                        
            elif end > root.key:
                if end == root.right.key:
                    print(str(root.right.key), end="") 
                    return 
                else:
                    print(str(root.right) + "," , end="")
                    self._depth(root.right, end)    
            
            elif end < root.key:
                if end == root.left.key:
                    print(str(root.left.key), end="") 
                    return
                else:
                    print(str(root.left.key) + "," , end="")
                    self._depth(root.left, end)
                    

        elif start < root.key:
            temp = root
            self._path(root.left, start, end, temp)
        elif start > root.key:
            temp = root
            self._path(root.right, start, end, temp)
    
    #Imprime los nodos hijos hacia abajo (No se necesita modificar)        
    def _depth(self, root, end):
        if end == root.key:
            return
        elif end > root.key:
            if root.right != None:                
                print(str(root.right.key) + "," , end="")
                self._depth(root.right, end)                  
        else:
            if root.left != None: 
                print(str(root.left.key) + "," , end="")
                self._depth(root.left, end)                              

#Crear arbol avl con las habitaciones
tree = AVLTree()
num = int(input())
for _ in range(num):
    room = input()
    tree.insert(room)
reco = int(input())
for _ in range(reco):    
    path = input()
    path = path.split()
    start = path[0]
    end = path[1]
    tree.path(start, end)
    print()