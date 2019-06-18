from tkinter import *
from tkinter import messagebox
import sqlite3
#Agregar las funciones
def conexion():
    miConexion=sqlite3.connect("Usuarios")
    miCursor= miConexion.cursor()
    try:
        miCursor.execute('''CREATE TABLE 
                    USUARIOS(
                    cod integer primary key autoincrement,                     
                    nom varchar(45),
                    ape varchar(45),
                    dir varchar(45),
                    dni varchar(8),
                    tel varchar(9),
                    com varchar(100)
                    )
                 ''')
        messagebox.showinfo("Conectar","Base de datos creada con éxito")
    except:
        messagebox.showwarning("Atención!!!","Base de datos ya existe")
def Salir():
    valor= messagebox.askquestion("Salir","Deseas salir de la aplicación")
    if valor=="yes":
        root.destroy()
def limpiarCampos():
    cod.set("")
    nom.set("")
    ape.set("")
    dir.set("")
    dni.set("")
    tel.set("")
    textoComentario.delete(1.0,END)


def crear():
    miConexion = sqlite3.connect("Usuarios")
    miCursor = miConexion.cursor()
    """miCursor.execute("INSERT INTO USUARIOS VALUES(NULL,'"+nom.get()+"','"+ape.get()+"','"+dir.get()+"','"+dni.get()+"','"+tel.get()+"','"+textoComentario.get("1.0",END)+"')")
    miConexion.commit()
    messagebox.showinfo("Confirmación","Registro grabado satisfactoriamente!!!")"""
    obj = nom.get(), ape.get(), dir.get(), dni.get(), tel.get(), textoComentario.get("1.0", END)

    miCursor.execute("INSERT INTO USUARIOS VALUES(Null,?,?,?,?,?,?)", (obj))
    miConexion.commit()
    messagebox.showinfo("Confirmación", "Registro grabado satisfactoriamente!!!")

def leer():
    miConexion=sqlite3.connect("Usuarios")
    miCursor= miConexion.cursor()
    miCursor.execute("SELECT * FROM USUARIOS WHERE cod='"+ cod.get()+"'")

    arreglo = miCursor.fetchall()
    for usu in arreglo:
        cod.set(usu[0])
        nom.set(usu[1])
        ape.set(usu[2])
        dir.set(usu[3])
        dni.set(usu[4])
        tel.set(usu[5])
        textoComentario.insert(1.0,usu[6])

    miConexion.commit()
def leerUltimoId():
    miConexion = sqlite3.connect("Usuarios")
    miCursor = miConexion.cursor()
    miCursor.execute("SELECT cod FROM USUARIOS ORDER BY cod DESC LIMIT 1")

    arreglo = miCursor.fetchall()

    cod.set(arreglo[0])

def modificar():
    miConexion=sqlite3.connect("Usuarios")
    miCursor= miConexion.cursor()
    miCursor.execute("UPDATE USUARIOS SET nom='"+nom.get()+"', ape='"+ape.get()+"', dir='"+dir.get()+"', dni='"+dni.get()+"',tel='"+tel.get()+"',com = '"+textoComentario.get("1.0",END)+"' WHERE cod='"+ cod.get() +"'")
    miConexion.commit()
    messagebox.showinfo("Confirmación","Registro actualizado satisfactoriamente!!!")

def eliminar():
    miConexion=sqlite3.connect("Usuarios")
    miCursor= miConexion.cursor()
    miCursor.execute("DELETE FROM USUARIOS WHERE cod="+ cod.get())
    miConexion.commit()
    messagebox.showinfo("Confirmación","Registro eliminado satisfactoriamente!!!")

#fin de crear las funciones

root=Tk()
#Crear la barra de menu
barraMenu =Menu(root)
root.config(menu=barraMenu,width=300,heigh=330)

bbddmenu=Menu(barraMenu,tearoff=0)
bbddmenu.add_command(label="Conectar",command=conexion)
bbddmenu.add_command(label="Salir",command=Salir)

borrarmenu=Menu(barraMenu,tearoff=0)
borrarmenu.add_command(label="Borrar Campos",command=limpiarCampos)

crudmenu=Menu(barraMenu,tearoff=0)
crudmenu.add_command(label="Crear",command=crear)
crudmenu.add_command(label="Leer",command=leer)
crudmenu.add_command(label="Actualizar",command=modificar)
crudmenu.add_command(label="Borrar",command=eliminar)

ayudamenu=Menu(barraMenu,tearoff=0)
ayudamenu.add_command(label="Licencia")
ayudamenu.add_command(label="Acerca de...")


barraMenu.add_cascade(label="BBDD", menu=bbddmenu)
barraMenu.add_cascade(label="Borrar", menu=borrarmenu)
barraMenu.add_cascade(label="CRUD", menu=crudmenu)
barraMenu.add_cascade(label="Ayuda", menu=ayudamenu)

#Diseñar campos


miFrame = Frame(root)
miFrame.pack()

cod     =   StringVar()
nom     =   StringVar()
ape     =   StringVar()
dir     =   StringVar()
dni     =   StringVar()
tel     =   StringVar()


cuadroCod=Entry(miFrame,textvariable=cod)
cuadroCod.grid(row=0,column=1,padx=10,pady=10)
cuadroCod.config(fg="gray",justify="left")

cuadroNombre=Entry(miFrame,textvariable=nom)
cuadroNombre.grid(row=1,column=1,padx=10,pady=10)
cuadroNombre.config(fg="red",justify="right")

cuadroApellido=Entry(miFrame,textvariable=ape)
cuadroApellido.grid(row=2,column=1,padx=10,pady=10)
cuadroApellido.config(fg="green",justify="right")

cuadroDireccion=Entry(miFrame,textvariable=dir)
cuadroDireccion.grid(row=3,column=1,padx=10,pady=10)
cuadroDireccion.config(fg="blue",justify="right")

cuadroDni=Entry(miFrame,textvariable=dni)
cuadroDni.grid(row=4,column=1,padx=10,pady=10)
cuadroDni.config(fg="red",justify="right")

cuadroTelefono=Entry(miFrame,textvariable=tel)
cuadroTelefono.grid(row=5,column=1,padx=10,pady=10)
cuadroTelefono.config(fg="blue",justify="right")

textoComentario=Text(miFrame,width=16,height=5)
textoComentario.grid(row=6,column=1,padx=10,pady=10)

scrollVert=Scrollbar(miFrame,command=textoComentario.yview)
scrollVert.grid(row=6,column=2,sticky="nsew")
textoComentario.config(yscrollcommand=scrollVert.set)


#LABEL
idlabel=Label(miFrame,text="Codigo:")
idlabel.grid(row=0,column=0,sticky="e",padx=10,pady=10)

nombreLabel=Label(miFrame,text="Nombres:")
nombreLabel.grid(row=1,column=0,sticky="e",padx=10,pady=10)

apellidoLabel=Label(miFrame,text="Apellidos:")
apellidoLabel.grid(row=2,column=0,sticky="e",padx=10,pady=10)

direccionLabel=Label(miFrame,text="Dirección:")
direccionLabel.grid(row=3,column=0,sticky="e",padx=10,pady=10)

dniLabel=Label(miFrame,text="DNI:")
dniLabel.grid(row=4,column=0,sticky="e",padx=10,pady=10)

telefonoLabel=Label(miFrame,text="Telefono:")
telefonoLabel.grid(row=5,column=0,sticky="e",padx=10,pady=10)

comentariosLabel=Label(miFrame,text="Comentarios:")
comentariosLabel.grid(row=6,column=0,sticky="e",padx=10,pady=10)

#Frames 2
miFrame2 = Frame(root)
miFrame2.pack()

botonCrear=Button(miFrame2,text="Create",command=crear)
botonCrear.grid(row=1,column=0,sticky="e",padx=10,pady=10)

botonLeer=Button(miFrame2,text="Read",command=leer)
botonLeer.grid(row=1,column=1,sticky="e",padx=10,pady=10)

botonActualizar=Button(miFrame2,text="Update",command=modificar)
botonActualizar.grid(row=1,column=2,sticky="e",padx=10,pady=10)

botonBorrar=Button(miFrame2,text="Delete",command=eliminar)
botonBorrar.grid(row=1,column=3,sticky="e",padx=10,pady=10)
#leerUltimoId()
root.mainloop()
