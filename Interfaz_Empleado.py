from customtkinter import *
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from ConexionBD import BaseDeDatos

#Clase que contiene el diseño de la ventana empleados
class Ventana_Empleado:
    def __init__(self,root,rol,vtn_empleado):
        self.root = root
        self.rol = rol
        self.root.title("Ventana Empleados")
        self.root.geometry("920x500")
        self.root.resizable(0,0)

        self.vtn_empleado = vtn_empleado


        set_appearance_mode("dark")
        set_default_color_theme("blue")

        #Diseño de la barra lateral de la ventana
        self.frame_lateral = CTkFrame(self.root,fg_color="blue",width=250,height=800)
        self.frame_lateral.place(x=0)

        self.label_titulo = CTkLabel(self.root,text="Menu Empleado",font=("Verdana",20,"bold"),fg_color="blue")
        self.label_titulo.place(x=40,y=10)

        self.label_id_pedido = CTkLabel(self.root,text="ID Pedido",font=("Verdana",15,"bold"),fg_color="blue")
        self.label_id_pedido.place(x=10,y=60)

        self.entry_id_pedido = Entry(self.root)
        self.entry_id_pedido.place(x=100,y=65)

        self.boton_buscar = Button(self.frame_lateral,text="BUSCAR",fg="red",command=self.Obtener_Datos)
        self.boton_buscar.place(x=100,y=120)

        self.boton_confirmar = CTkButton(self.root,text="Confirmar Compra",fg_color="blue2",font=("Arial",15,),width=150,height=40)
        self.boton_confirmar.place(x=400,y=300)

        self.boton_cancelar = CTkButton(self.root,text="Cancelar Compra",fg_color="blue2",font=("Arial",15,),width=150,height=40)
        self.boton_cancelar.place(x=600,y=300)
        
        columnas = ("Medicamento","Cantidad","Metodo De Pago","Estado","Total")

        #Diseño de la seccion donde se implementara la tabla
        self.tabla = ttk.Treeview(self.root,columns=columnas,show="headings")

        self.tabla.heading("Medicamento",text="Medicamento")
        self.tabla.heading("Cantidad",text="Cantidad")
        self.tabla.heading("Metodo De Pago",text="Metodo De Pago")
        self.tabla.heading("Estado",text="Pago")
        self.tabla.heading("Total",text="Total")

        self.tabla.column("Medicamento",width=130,anchor="center")
        self.tabla.column("Cantidad",width=130,anchor="center")
        self.tabla.column("Metodo De Pago",width=130,anchor="center")
        self.tabla.column("Estado",width=130,anchor="center")
        self.tabla.column("Total",width=130,anchor="center")

        self.tabla.place(x=255,y=10)

    def Obtener_Datos(self):
        bd = BaseDeDatos(host="localhost",user="root",password="Soydeboca66",database="Farmacia")
        bd.CrearConexion()

        id_pedido = self.entry_id_pedido.get()

        query = "SELECT m.Nombre AS Nombre_Producto,dp.Cantidad,p.Metodo_pago,p.Estado,p.Total FROM Pedidos p JOIN Detalle_Pedidos dp ON p.id_pedido = dp.id_pedido JOIN Medicamentos m ON dp.id_medicamento = m.id_medicamento WHERE p.id_pedido = %s"
        try:
            resultados = bd.ObtenerDatos(query,(id_pedido,))
            self.tabla.delete(*self.tabla.get_children())

            if not id_pedido:
                messagebox.showwarning("Advertencia","Por favor ingrese un ID de pedido")
                return

            if resultados:
                for datos in resultados:
                    self.tabla.insert("","end",values=datos)
                    self.entry_id_pedido.delete(0,END)
            else:
                messagebox.showwarning("Advertencia","ID de pedido inexistente")
                self.entry_id_pedido.delete(0,END)
        except Exception as err:
            messagebox.showerror("Error","Error interno al obtener los datos")
            print(err)

