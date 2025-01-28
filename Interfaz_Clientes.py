from customtkinter import *
from tkinter import *
from tkinter import messagebox
from PIL import Image,ImageTk
from ConexionBD import BaseDeDatos
from tkinter import ttk

class Ventana_Clientes:
    def __init__(self,root,vtn_clientes,dni_cliente):
        self.root = root
        self.root.title("Ventana Clientes")
        self.root.geometry("1200x500")
        self.root.resizable(0,0)

        self.vtn_clientes = vtn_clientes


        bd = BaseDeDatos(host="localhost",user="root",password="Soydeboca66",database="Farmacia")

        bd.CrearConexion()

        query = "SELECT Nombre,Apellido,DNI,Obra_Social FROM Clientes WHERE DNI = %s"
        params = (dni_cliente,)
        
        resultados = bd.ObtenerDatos(query,params)


        set_appearance_mode("system")
        set_default_color_theme("green")

        self.frame_lateral = CTkFrame(self.root,fg_color="purple4",height=500,width=250,corner_radius=10)
        self.frame_lateral.place(x=0)

        self.label_datos = CTkLabel(self.frame_lateral,text="Datos Cliente",text_color="black",font=("Comic Sans MS",25,"bold"))
        self.label_datos.place(x=40,y=5)

        imagen_cliente = Image.open("C:\\Users\\Luis Robles\\Desktop\\ProyectoFinal_Cursos2024\\cliente.png")
        imagen_cliente = imagen_cliente.resize((200,200))
        imagen_tk = ImageTk.PhotoImage(imagen_cliente)

        self.imagen = CTkLabel(self.frame_lateral,image=imagen_tk,text="")
        self.imagen.place(x=30,y=50)
        
        self.nombre = CTkLabel(self.frame_lateral,text=f"Nombre: {resultados[0][0]} {resultados[0][1]}",text_color="black",font=("Comic Sans MS",15))
        self.nombre.place(x=30,y=240)

        self.label_DNI = CTkLabel(self.frame_lateral,text=f"DNI: {resultados[0][2]}",text_color="black",font=("Comic Sans MS",15))
        self.label_DNI.place(x=30,y=260)
        
        self.label_obrasocial = CTkLabel(self.frame_lateral,text=f"Obra Social: {resultados[0][3]}",text_color="black",font=("Comic Sans MS",15))
        self.label_obrasocial.place(x=30,y=280)

        self.boton_salir = CTkButton(self.frame_lateral,text="SALIR",fg_color="green2",text_color="black")
        self.boton_salir.place(x=30,y=420)

        self.imagen.image = imagen_tk
        columnas = ("Nombre","Descripcion","Precio","Categoria")
        self.tree = ttk.Treeview(self.root,columns=columnas,show="headings")

        self.tree.heading("Nombre",text="Nombre")
        self.tree.heading("Descripcion",text="Descripcion")
        self.tree.heading("Precio",text="Precio")
        self.tree.heading("Categoria",text="Categoría")

        self.tree.column("Nombre",width=130,anchor="center")
        self.tree.column("Descripcion",width=130,anchor="center")
        self.tree.column("Precio",width=130,anchor="center")
        self.tree.column("Categoria",width=145,anchor="center")

        self.tree.place(x=255,y=10)
        
        query = "SELECT Nombre,Descripcion,Precio,Categoria FROM Medicamentos"
        medicamentos = bd.ObtenerDatos(query,())

        for medicamento in medicamentos:
            self.tree.insert("","end",values=medicamento)

        columnas_tablaf = ("Nombre","Precio")
        self.tabla_final = ttk.Treeview(self.root,columns=columnas_tablaf,show="headings")

        self.tabla_final.heading("Nombre",text="Nombre")
        self.tabla_final.heading("Precio",text="Precio")

        self.tabla_final.column("Nombre",width=130,anchor="center")
        self.tabla_final.column("Precio",width=130,anchor="center")

        self.tabla_final.place(x=850,y=10)

        self.boton_agregar = CTkButton(self.root,text="Agregar",fg_color="blue",command=self.Agregar_Producto)
        self.boton_agregar.place(x=255,y=250)

        self.boton_eliminar = CTkButton(self.root,text="Eliminar",fg_color="blue",command=self.Eliminar_Producto)
        self.boton_eliminar.place(x=400,y=250)

    def Agregar_Producto(self):
        item_seleccionado = self.tree.selection()
        if item_seleccionado:
            medicamento = self.tree.item(item_seleccionado)["values"]
            self.tabla_final.insert("","end",values=(medicamento[0],medicamento[2]))
        else:
            messagebox.showwarning("Advertencia","Por favor seleccione un medicamento")
    def Eliminar_Producto(self):
        item = self.tabla_final.selection()
        if item:
            medicamento = self.tabla_final.item(item)["values"]
            self.tabla_final.delete(item)
        else:
            messagebox.showwarning("Advertencia","Por favor seleccione el medicamento a eliminar")
    
        