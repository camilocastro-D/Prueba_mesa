# Importar Bibliotecas
from tkinter import *
import tkinter as tk	
from tkinter import messagebox as mb
from tkinter import ttk 
import sqlite3
from tkinter import messagebox

conn=sqlite3.connect('login.db')
c=conn.cursor()

def create_table():
	c.execute("CREATE TABLE IF NOT EXISTS empleados(Nombre TEXT,Apellido TEXT ,Usuario TEXT,Contraseña TEXT)")
	conn.commit()
	c.close()
	conn.close()

create_table()

ventana=tk.Tk()
ventana.title("Inicio de secion")	
ventana.geometry("280x450+300+250")	
	
color='#DC143C'			
ventana['bg']=color		

Label(ventana,bg=color,text="Login",font=("Arial Black",16)).pack()	


#Cajas de nuestra ventana Principal
Label(ventana,text="Usuario : ",bg=color,font=("Arial Black",10)).pack()	
caja1=Entry(ventana,font=("Arial",10))										
caja1.pack()																
Label(ventana,text="Contraseña : ",bg=color,font=("Arial Black",10)).pack()	
caja2=Entry(ventana,show="*")												
caja2.pack()																

db=sqlite3.connect('login.db')		
c=db.cursor()						

def login():				
	usuario=caja1.get()		
	contr=caja2.get()		
	c.execute('SELECT * FROM empleados WHERE Usuario = ? AND Contraseña = ?',(usuario,contr))	
	if c.fetchall():
		mb.showinfo(title="Login Correcto",message="Usuario y contraseña correctos")		
		ventana.destroy()
	else:
		mb.showerror(title="Login incorrecto",message="Usuario o contraseña incorrecto")	
	#c.close()

def nuevaVentana():							
	newVentana=tk.Toplevel(ventana)			
	newVentana.title("Registro de Usuario")	
	newVentana.geometry("300x290+800+250")	
	newVentana['bg']=color					
	
	labelExample=tk.Label(newVentana,text="Registro : ",bg=color,font=("Arial Black",12)).pack(side="top")	
	

	Label(newVentana,text="Nombre : ",bg=color,font=("Arial Black",10)).pack()		
	caja3=Entry(newVentana)															
	caja3.pack()
	Label(newVentana,text="Apellidos : ",bg=color,font=("Arial Black",10)).pack()	
	caja4=Entry(newVentana)															
	caja4.pack()
	Label(newVentana,text="Usuario : ",bg=color,font=("Arial Black",10)).pack()		
	caja5=Entry(newVentana)															
	caja5.pack()
	Label(newVentana,text="Contraseña : ",bg=color,font=("Arial Black",10)).pack()	
	caja6=Entry(newVentana,show="*")												
	caja6.pack()	
	Label(newVentana,text="Repita la Contraseña : ",bg=color,font=("Arial Black",10)).pack()	
	caja7=Entry(newVentana,show="*")															 
	caja7.pack()
	def registro():				
		Nombre=caja3.get()		
		Apellido=caja4.get()	
		Usr_reg=caja5.get()		
		Contra_reg=caja6.get()	
		Contra_reg_2=caja7.get() 
		if(Contra_reg==Contra_reg_2):		
			
			c.execute("INSERT INTO empleados values(\'"+Nombre+"\',\'"+Apellido+"\',\'"+Usr_reg+"\',\'"+Contra_reg+"')")
			db.commit()			#Confirmamos los datos
			mb.showinfo(title="Registro Correcto",message="Hola "+Nombre+" "+Apellido+" ¡¡ \nSu registro fue exitoso.")
			newVentana.destroy()		#Cerramos la ventana de registro
		else:	#Se ejecutara si las contraseñas no coinciden
			mb.showerror(title="Contraseña Incorrecta",message="Error¡¡¡ \nLas contraseñas no coinciden.")	#Mostramos un mensaje

	#El siguiente comando (boton) nos permite llamar a la funcion registro
	buttons=tk.Button(newVentana,text="Registro",command=registro,bg=color,font=("Arial Rounded MT Bold",10)).pack(side="bottom")
	
Label(ventana,text=" ",bg=color,font=("Arial",10)).pack()		 
Button(text=" ENTRAR ",command=login,bg='#a6d4f2',font=("Arial Rounded MT Bold",10)).pack()		
Label(ventana,text=" ",bg=color,font=("Arial Black",10)).pack()
Label(ventana,text="¿No tienes una cuenta? ",bg=color,font=("Arial Black",10)).pack()		
#La siguiente linea (boton) nos llama a la funcion 'nuevaVentana' ==> ( ventana de registro)
boton1=Button(ventana,text="REGISTRATE",bg='#a6d4f2',command=nuevaVentana,font=("Arial Rounded MT Bold",10)).pack()

ventana.mainloop()

root=Tk()
root.title("Registro de clintes")
root.geometry("350x300")

miDocumento=StringVar()
miNombre=StringVar()
miApellido=StringVar()
miCodigopostal=StringVar()
miDireccion=StringVar()

def conexionBBDD():
    

    miConexion=sqlite3.connect("UsuariosDB")
    miCursor=miConexion.cursor()
    
    try:
        
        miCursor.execute('''
            CREATE TABLE DATOSUSUARIOS (
            DOCUMENTO INTEGER PRIMARY KEY AUTOINCREMENT,
            NOMBRE_USUARIO VARCHAR(50),
            CODIGO VARCHAR(50),
            APELLIDO VARCHAR(20),
            DIRECCION VARCHAR(50))
            
            ''')
        #COMENTARIOS VARCHAR(100))
        
        
        messagebox.showinfo("BBDD","BBDD creada con éxito")
    
    except:
        
        messagebox.showwarning("¡Atención!","La BBDD ya existe")


def salirAplicacion():
    
    valor=messagebox.askquestion("Salir","¿Deseas salir de la aplicación?")
    if valor=="yes":
        root.destroy()
        
def limpiarCampos():
    miDocumento.set("")
    miNombre.set("")
    miApellido.set("")
    miDireccion.set("")
    miCodigopostal.set("")
    
    
    
def mensaje():
    print("Castro Camilo, Sistema de ventas desarrollado en Python 3.7")

    
    
def crear():
    miConexion=sqlite3.connect("UsuariosDB")
    miCursor=miConexion.cursor()
    
    datos=miNombre.get(),miCodigopostal.get(),miApellido.get(),miDireccion.get()
    miCursor.execute("INSERT INTO DATOSUSUARIOS VALUES(NULL,?,?,?,?)", (datos))
    
    miConexion.commit()
    
    messagebox.showinfo("BBDD","Registro insertado con éxito")


    
    
def leer():
    
    miConexion=sqlite3.connect("UsuariosDB")
    miCursor=miConexion.cursor()
    miCursor.execute("SELECT * FROM DATOSUSUARIOS WHERE DOCUMENTO=" +miDocumento.get())
    elUsuario=miCursor.fetchall()
    
    for usuario in elUsuario:
        
        miDocumento.set(usuario[0])
        miNombre.set(usuario[1])
        miApellido.set(usuario[3])
        miDireccion.set(usuario[4])
    
    
    miConexion.commit()

    
def actualizar():
    
    miConexion=sqlite3.connect("UsuariosDB")
    miCursor=miConexion.cursor()
    
    datos=miNombre.get(),miCodigopostal.get(),miApellido.get(),miDireccion.get()
    
    miCursor.execute("UPDATE DATOSUSUARIOS SET NOMBRE_USUARIO=?, CODIGO=?, APELLIDO=?, DIRECCION=? "+
    
    "WHERE DOCUMENTO=" + miDocumento.get(),(datos))
    
    
    
    
    
    miConexion.commit()
    
    messagebox.showinfo("BBDD","Registro actualizado con éxito")
    
    
def borrar():
    
    miConexion=sqlite3.connect("UsuariosDB")
    miCursor=miConexion.cursor()
    miCursor.execute("DELETE FROM DATOSUSUARIOS WHERE ID=" +miDocumento.get())
                    
    miConexion.commit()
    
    messagebox.showinfo("BBDD","Registro borrado con éxito")
    
    
menubar=Menu(root)
menubasedat=Menu(menubar, tearoff=0)
menubasedat.add_command(label="Conectar", command=conexionBBDD)
menubasedat.add_command(label="Salir", command=salirAplicacion)
menubar.add_cascade(label="BBDD", menu=menubasedat)


menuborrar=Menu(menubar, tearoff=0)
menuborrar.add_command(label="Borrar campos", command=limpiarCampos)
menubar.add_cascade(label="Borrar",menu=menuborrar )


ayudamenu=Menu(menubar, tearoff=0)
ayudamenu.add_command(label="Licencia", command=mensaje)
ayudamenu.add_command(label="Acerca", command=mensaje)
menubar.add_cascade(label="Ayuda", menu=ayudamenu)

root.config(menu=menubar)

l1=Label(root, text="Documento: ")
l1.grid(column=0, row=1)


e1=Entry(root, textvariable=miDocumento)
e1.grid(column=1, row=1)

l2=Label(root, text="Nombre: ")
l2.grid(column=0, row=2)


e2=Entry(root, textvariable=miNombre)
e2.grid(column=1, row=2)

l3=Label(root, text="Codigo postal: ")
l3.grid(column=0, row=3)

e3=Entry(root,textvariable=miCodigopostal)
e3.grid(column=1, row=3)

l4=Label(root, text="Apellido: ")
l4.grid(column=0, row=4)

e4=Entry(root,textvariable=miApellido)
e4.grid(column=1, row=4)

l5=Label(root, text="Dirección: ")
l5.grid(column=0, row=5)

e5=Entry(root,textvariable=miDireccion)
e5.grid(column=1, row=5)





b1=Button(root, text="Crear",bg='#FFC0CB', command=crear)
b1.place(x=40,y=250)

b2=Button(root, text="Borrar",bg='#FFC0CB', command=borrar)
b2.place(x=180,y=250)

root.mainloop()
