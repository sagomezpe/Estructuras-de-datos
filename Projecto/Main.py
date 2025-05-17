from Projecto import Estructuras
import time
from tkinter import *
from tkinter import messagebox
from datetime import datetime

def checkFileExistance(filePath):

    try:
        with open(filePath, 'r') as f:
            return True
    except FileNotFoundError as e:
        return False
    except IOError as e:
        return False              

def crear():
    User = cajaNombre.get()
    Pass = cajaClave.get()
    if User != "" and Pass != "":    
        bool = hash.insert(User, Pass)
        if bool == True:
            messagebox.showinfo("", "Usuario Creado")
            #Guardar lista encadenada
            hash.save(link)            
            #Cerrar usuarios txt
            user = open("user.txt", "w")        
            while link.head != None:        
                user_name = link.PopFront()
                user.write(user_name)
                user.write("\n")
                
            #Abrir usuarios txt 
            user = open("user.txt", "r")
            for line in user:
                x = line.split()
                hash.insert(str(x[0]),str(x[1]))

        else:
            messagebox.showinfo("","Nombre de usuario ya registrado")    
    else:
        messagebox.showerror("Error","No puede dejar espacios en blanco")
    
def acceder():
    User = cajaNombre.get()
    Pass = cajaClave.get()
    case = hash.search(User, Pass)
    if case == 0:
        #Fichero de articulos
        bool_art = checkFileExistance(str(User)+"_articulos.txt")
        if bool_art == True:
            art = open(str(User)+"_articulos.txt", "r")
            for line in art:
                x = line.split()
                tree.insert(x[0],int(x[1]),float(x[2]),float(x[3]))
        else:     
            art = open(str(User)+"_articulos.txt", "w")
                    
        #Fichero de transacciones    
        bool_trans = checkFileExistance(str(User)+"_transacciones.txt")
        if bool_trans == True:
            trans = open(str(User)+"_transacciones.txt", "r")
            for line in trans:    
                x = line.split()
                fecha_list = x[4:9]
                fecha = " ".join(fecha_list)
                stack.push(x[0],int(x[1]),float(x[2]),float(x[3]), fecha)
        else:     
            trans = open(str(User)+"_transacciones.txt", "w")
                                                        
        raiz1.withdraw()
        raiz2.deiconify()
            
    if case == 1:
        messagebox.showinfo("", "Clave incorrecta")
    if case == 2:
        messagebox.showinfo("", "El usuario no existe")    
    
def salir():
    raiz1.quit()        

def agregar():
    name = cajaArticulo.get()
    if name != "":    
        tree.insert(name, 0, 0, 0)
    else:
        messagebox.showerror("Error","No puede dejar espacios en blanco")
    
def eliminar():
    name = cajaArticulo.get()
    if name != "":          
        tree.delete(name)
    else:
        messagebox.showerror("Error","No puede dejar espacios en blanco")
    
def comprar():
    name = cajaArticulo.get()
    num = cajaNumero.get()    
    price = cajaCosto.get()
    if name != "" and num != "" and price!= "":
        if num.isnumeric() == True and price.isnumeric():
            num = int(num)
            price = float(price)
            if num <= 0:
                messagebox.showerror("Error", "El numero de elementos debe ser positivo")
            elif price <= 0:
                messagebox.showerror("Error", "El costo de la transaccion debe ser positivo")
            else:        
                tree.buy(name, num, price, stack)
        else:
            messagebox.showerror("Error", "Ingreso de caracteres en espacios numericos")
    else:
        messagebox.showerror("Error","No puede dejar espacios en blanco")
    
def vender():
    name = cajaArticulo.get()
    num = cajaNumero.get()
    price = cajaIngreso.get()
    if name != "" and num != "" and price!= "":
        if num.isnumeric() == True and price.isnumeric():
            num = int(num)
            price = float(price)
            if num <= 0:
                messagebox.showerror("Error", "El numero de elementos debe ser positivo")
            elif price <= 0:
                messagebox.showerror("Error", "El ingreso de la transaccion debe ser positivo")
            else:        
                tree.sell(name, num, price, stack)
        else:
            messagebox.showerror("Error", "Ingreso de caracteres en espacios numericos")
    else:
        messagebox.showerror("Error","No puede dejar espacios en blanco")
    
def buscar():
    name = cajaArticulo.get()
    if name != "":
        tree.search(name)
    else:
        messagebox.showerror("Error","No puede dejar espacios en blanco")
    
def listado():
    tree.inOrder() 
    
def transacciones():
    stack.print()
    
def cerrar():
    User = cajaNombre.get()
    tree.saveQueue(tree.root, queue)
    art = open(str(User)+"_articulos.txt",'w')
    trans = open(str(User)+"_transacciones.txt",'w')
            
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
    
    raiz2.withdraw()
    raiz1.deiconify()
    
raiz1 = Tk()

frame1 = Frame(raiz1, width = 1200, height = 600)
frame1.pack()

textoNombre = Label(frame1, text = "Usuario")
textoNombre.grid(row = 0, column = 0, padx = 10, pady = 10)

textoClave = Label(frame1, text = "Clave")
textoClave.grid(row = 1, column = 0, padx = 10, pady = 10)

cajaNombre = Entry(frame1)
cajaNombre.grid(row = 0, column = 2, padx = 10, pady = 10)

cajaClave = Entry(frame1)
cajaClave.grid(row = 1, column = 2, padx = 10, pady = 10)

botonUsuario = Button(frame1, text = "Crear Usuario", command = crear)
botonUsuario.grid(row = 2, column = 0, padx = 10, pady = 10)

botonAcceder = Button(frame1, text = "Acceder", command = acceder)
botonAcceder.grid(row = 2, column = 1, padx = 30, pady = 10)

botonSalir = Button(frame1, text = "Salir", command = salir)
botonSalir.grid(row = 2, column = 2, padx = 10, pady = 10)

raiz2 = Tk()
raiz2.withdraw()

frame2 = Frame(raiz2, width = 1200, height = 600)
frame2.pack()

botonAgregar = Button(frame2, text = "Agregar", command = agregar)
botonAgregar.grid(row = 0, column = 0, padx = 10, pady = 10)

botonEliminar = Button(frame2, text = "Eliminar", command = eliminar)
botonEliminar.grid(row = 0, column = 1, padx = 10, pady = 10)

botonComprar = Button(frame2, text = "Comprar", command = comprar)
botonComprar.grid(row = 0, column = 2, padx = 10, pady = 10)

botonVender = Button(frame2, text = "Vender", command = vender)
botonVender.grid(row = 0, column = 3, padx = 10, pady = 10)

botonBuscar = Button(frame2, text = "Buscar", command = buscar)
botonBuscar.grid(row = 1, column = 0, padx = 10, pady = 10)

botonListado = Button(frame2, text = "Productos en registro", command = listado)
botonListado.grid(row = 1, column = 1, padx = 10, pady = 10)

botonAgregar = Button(frame2, text = "Transacciones realizadas", command = transacciones)
botonAgregar.grid(row = 1, column = 2, padx = 10, pady = 10)

botonCerrar = Button(frame2, text = "Cerrar sesion", command = cerrar)
botonCerrar.grid(row = 1, column = 3, padx = 10, pady = 10)

textoArticulo = Label(frame2, text = "Nombre")
textoArticulo.grid(row = 2, column = 1, padx = 10, pady = 10)

textoNumero = Label(frame2, text = "Numero")
textoNumero.grid(row = 3, column = 1, padx = 10, pady = 10)

textoCosto = Label(frame2, text = "Costo")
textoCosto.grid(row = 4, column = 1, padx = 10, pady = 10)

textoIngreso = Label(frame2, text = "Ingreso")
textoIngreso.grid(row = 5, column = 1, padx = 10, pady = 10)

cajaArticulo = Entry(frame2)
cajaArticulo.grid(row = 2, column = 2, padx = 10, pady = 10)

cajaNumero = Entry(frame2)
cajaNumero.grid(row = 3, column = 2, padx = 10, pady = 10)

cajaCosto = Entry(frame2)
cajaCosto.grid(row = 4, column = 2, padx = 10, pady = 10)

cajaIngreso = Entry(frame2)
cajaIngreso.grid(row = 5, column = 2, padx = 10, pady = 10)


hash = Estructuras.HashTable()
tree = Estructuras.AVLTree()
queue = Estructuras.Queue()
stack = Estructuras.Stack()
link = Estructuras.LinkedList()

#Abrir usuarios txt
bool_user = checkFileExistance("user.txt")
if bool_user == True:
    user = open("user.txt", "r")
    for line in user:
        x = line.split()
        hash.insert(str(x[0]),str(x[1]))
else:     
    user = open("user.txt", "w+")

raiz1.mainloop() 

#Cerrar usuarios txt
hash.save(link)
user = open("user.txt", "w")        
while link.head != None:        
    user_name = link.PopFront()
    user.write(user_name)
    user.write("\n")
user.close()


print("Los datos se han guardado")
print("Programa finalizado")          
