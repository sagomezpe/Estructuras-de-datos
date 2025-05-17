import time

class TreeNode(object):
    def __init__(self, data):
        self.data = data
        self.num = 0
        self.expenses = 0
        self.incomes = 0
        self.left = None
        self.right = None
        self.height = 1

class AVLTree(object):

    def __init__(self):
        self.root = None 

    def insert(self, data, num, expenses, incomes):
        self.root = self.insert_node(self.root, data, num, expenses, incomes)   

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

a = AVLTree()

for i in range(10000000):
    a.insert(i, 0,0,0)

inicio = time.time()

a.inOrder(a.root)

fin = time.time()

print(fin-inicio)                                        