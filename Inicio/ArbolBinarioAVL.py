# AVL tree implementation in Python


import sys

# Create a tree node
class TreeNode(object):
    def __init__(self, num, grade, prom):
        self.num = num
        self.grade = grade
        self.prom = prom
        self.left = None
        self.right = None
        self.height = 1


class AVLTree(object):

    # Function to insert a node
    def insert_node(self, root, num, grade, prom):

        # Find the correct location and insert the node
        if not root:
            return TreeNode(num, grade, prom)
        elif num < root.num:
            root.left = self.insert_node(root.left, num, grade, prom)
        elif num > root.num:
            root.right = self.insert_node(root.right, num, grade, prom)
        else:
            return print("Se encontro un estudiante con el mismo numero de identificacion")    

        root.height = 1 + max(self.getHeight(root.left),
                              self.getHeight(root.right))

        # Update the balance factor and balance the tree
        balanceFactor = self.getBalance(root)
        if balanceFactor > 1:
            if num < root.left.num:
                return self.rightRotate(root)
            else:
                root.left = self.leftRotate(root.left)
                return self.rightRotate(root)

        if balanceFactor < -1:
            if num > root.right.num:
                return self.leftRotate(root)
            else:
                root.right = self.rightRotate(root.right)
                return self.leftRotate(root)

        return root
    
# Function to delete a node
    def delete_node(self, root, key):

        # Find the node to be deleted and remove it
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
            root.right = self.delete_node(root.right,
                                          temp.key)
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

    def inOrder(self, root):
        if not root:
            return
        self.inOrder(root.left)
        print("Numero de identificacion " + str(root.num) + " grado " + str(root.grade) + " promedio " + str(root.prom))
        self.inOrder(root.right)

myTree = AVLTree()
root = None
user = True

while user == True:
    print("1 agregar estudiante")
    print("2 eliminar estudiante")    
    print("3 ver datos de estudiantes")
    op = input()
    if op.isnumeric() == True:
        op = int(op)
        
        if op == 1:
            print("Inserte Numero de identificacion")
            num = int(input())
            print("Inserte grado del estudiante")
            grade = input()
            print("Inserte promedio del estudiante")
            prom = input()
            root = myTree.insert_node(root, num, grade, prom)              
                        
        elif op == 2:
            print("Inserte Numero de identificacion")
            root = myTree.delete_node(root, num) 
                
        elif op == 3:
            myTree.inOrder(root)                
        else:
            print("Ha ingresado un valor erroneo")
    else:          
        print("Error, no ha ingresado un numero")     
    print("Si desea realizar otra operacion, ingrese 1, para salir presione otro numero")       
    program = int(input())
    if program != 1:
        user = False
print("Programa finalizado")               