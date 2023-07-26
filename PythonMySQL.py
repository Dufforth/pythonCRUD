import  tkinter as tk

from tkinter import *

from tkinter import ttk
from tkinter import messagebox

from Clientes import *
from Conexion import *


class ClientForm:
 global base
 base = None

 global texBoxId
 texBoxId = None

 global textBoxNombres
 textBoxNombres = None

 global textBoxApellidos
 textBoxApellidos = None

 global combo
 combo = None


 global groupBox
 groupBox = None

 global tree
 tree = None

def Form():
  global base
  global textBoxId
  global textBoxNombres
  global textBoxApellidos
  global combo
  global groupBox
  global tree

  try:
            base= Tk()
            base.geometry("1200x300")
            base.title("Formulario")

            groupBox = LabelFrame(base, text="Datos del Personal", padx=5,pady=5)
            groupBox.grid(row=0,column=0,padx=10,pady=10)

            labelId=Label(groupBox,text="Id:",width=13,font=("arial",12)).grid(row=0,column=0)
            textBoxId = Entry(groupBox)
            textBoxId.grid(row=0,column=1)

            labelNombre=Label(groupBox,text="Nombre:",width=13,font=("arial",12)).grid(row=1,column=0)
            textBoxNombres = Entry(groupBox)
            textBoxNombres.grid(row=1,column=1)

            labelApellido=Label(groupBox,text="Apellido",width=13,font=("arial",12)).grid(row=2,column=0)
            textBoxApellidos = Entry(groupBox)
            textBoxApellidos.grid(row=2,column=1)

            labelSexo=Label(groupBox,text="Sexo",width=13,font=("arial",12)).grid(row=3,column=0)
            SelectSex = tk.StringVar()
            combo= ttk.Combobox(groupBox,values=["Masculino","Femenino"], textvariable=SelectSex)
            combo.grid(row=3,column=1)
            SelectSex.set("Masculino")

            Button(groupBox,text="Guardar",width=10, command=guardarRegistros).grid(row=4,column=0)
            Button(groupBox,text="Modificar",width=10, command=modificarRegistros).grid(row=4,column=1)
            Button(groupBox,text="Eliminar",width=10, command=eliminarRegistros).grid(row=4,column=2)

            groupBox = LabelFrame(base, text="Lista del personal", padx=5,pady=5)
            groupBox.grid(row=0,column=1,padx=10,pady=10)


            tree= ttk.Treeview(groupBox,columns=("Id","Nombre","Apellido","Sexo"),show='headings',height=5)
            tree.column("# 1", anchor=CENTER)
            tree.heading("# 1", text="Id")
            tree.column("# 2", anchor=CENTER)
            tree.heading("# 2", text="Nombre")
            tree.column("# 3", anchor=CENTER)
            tree.heading("# 3", text="Apellido")
            tree.column("# 4", anchor=CENTER)
            tree.heading("# 4", text="Sexo")

            for row in CClientes.mostrarClientes():
                tree.insert("","end", values=row)

            tree.bind("<<TreeviewSelect>>", seleccionarRegistro)

            tree.pack()

            base.mainloop()

  except ValueError as error:
            print("Error al mostrar la interfaz, error:{}".format(error))

def guardarRegistros():
       global textBoxNombres,textBoxApellidos,combo,groupBox

       try:
             if textBoxNombres is None or textBoxApellidos is None or combo is None:
                   print("Los widgets no estan inicializados")
                   return 
             
             nombres = textBoxNombres.get()
             apellidos = textBoxApellidos.get()
             sexo = combo.get()

             CClientes.ingresarClientes(nombres,apellidos,sexo)
             messagebox.showinfo("Informacion","Los datos fueron guardados")

             actualizarTreeView()

             textBoxNombres.delete(0,END)
             textBoxApellidos.delete(0,END)


       except ValueError as error:
             print("error al ingresar los datos {}".format(error))

def actualizarTreeView():
      global tree
      try:
        tree.delete(*tree.get_children())      

        datos = CClientes.mostrarClientes()
        
        for row in CClientes.mostrarClientes():
                tree.insert("","end", values=row)
      
      except ValueError as error:
            print("error al actualizar tabla {}".format(error))

def seleccionarRegistro(event):
    try:
          itemSeleccionado=  tree.focus()

          if itemSeleccionado:
                values = tree.item(itemSeleccionado)['values']

                textBoxId.delete(0,END)
                textBoxId.insert(0,values[0])
                textBoxNombres.delete(0,END)
                textBoxNombres.insert(0,values[1])
                textBoxApellidos.delete(0,END)
                textBoxApellidos.insert(0,values[2])
                combo.set(values[3])

    except ValueError as error:
          print("Error al seleccionar registro {}".format())

def modificarRegistros():
       global textBoxId,textBoxNombres,textBoxApellidos,combo,groupBox

       try:
             if textBoxId is None or textBoxNombres is None or textBoxApellidos is None or combo is None:
                   print("Los widgets no estan inicializados")
                   return 
             
             idUsuario= textBoxId.get()
             nombres = textBoxNombres.get()
             apellidos = textBoxApellidos.get()
             sexo = combo.get()

             CClientes.modificarClientes(idUsuario,nombres,apellidos,sexo)
             messagebox.showinfo("Informacion","Los datos fueron actualizados")

             actualizarTreeView()
             textBoxId.delete(0,END)
             textBoxNombres.delete(0,END)
             textBoxApellidos.delete(0,END)


       except ValueError as error:
             print("error al actualizar los datos {}".format(error))

def eliminarRegistros():
       global textBoxId,textBoxNombres,textBoxApellidos

       try:
             if textBoxId is None:
                   print("Los widgets no estan inicializados")
                   return 
             
             idUsuario= textBoxId.get()

             CClientes.eliminarClientes(idUsuario)
             messagebox.showinfo("Informacion","Los datos fueron eliminados")

             actualizarTreeView()
             textBoxId.delete(0,END)
             textBoxNombres.delete(0,END)
             textBoxApellidos.delete(0,END)


       except ValueError as error:
             print("error al eliminar los datos {}".format(error))


Form()