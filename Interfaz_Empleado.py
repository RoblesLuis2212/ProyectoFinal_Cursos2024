from customtkinter import *
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from ConexionBD import BaseDeDatos
import random
from Cifrado import Cifrar_Contraseña

#Clase que contiene el diseño de la ventana empleados
class Ventana_Empleado:
    def __init__(self,root,rol,vtn_empleado):
        self.root = root
        self.rol = rol
        self.root.title("Ventana Empleados")
        self.root.geometry("920x400")
        self.root.resizable(0,0)

        self.vtn_empleado = vtn_empleado


        set_appearance_mode("dark")
        set_default_color_theme("blue")

        #Diseño de la barra lateral de la ventana
        self.frame_lateral = CTkFrame(self.root,fg_color="black",width=250,height=800)
        self.frame_lateral.place(x=0)

        self.label_titulo = CTkLabel(self.root,text="Menu Empleado",font=("Verdana",20,"bold"),fg_color="black")
        self.label_titulo.place(x=40,y=10)

        self.label_id_pedido = CTkLabel(self.root,text="ID Pedido",font=("Verdana",15,"bold"),fg_color="black")
        self.label_id_pedido.place(x=10,y=60)

        self.entry_id_pedido = Entry(self.root)
        self.entry_id_pedido.place(x=100,y=65)

        self.boton_confirmar = CTkButton(self.root,text="Confirmar Compra",fg_color="blue2",font=("Arial",15,),width=150,height=40)
        self.boton_confirmar.place(x=260,y=250)

        self.boton_cancelar = CTkButton(self.root,text="Cancelar Compra",fg_color="blue2",font=("Arial",15,),width=150,height=40)
        self.boton_cancelar.place(x=420,y=250)

        self.boton_limpiar = CTkButton(self.root,text="Limpiar Tabla",fg_color="blue2",font=("Arial",15),width=150,height=40,command=self.Limpiar_Tabla)
        self.boton_limpiar.place(x=580,y=250)

        self.boton_buscar = CTkButton(self.frame_lateral,text="BUSCAR",fg_color="blue2",width=185,command=self.Obtener_Datos)
        self.boton_buscar.place(x=40,y=100)
        
        self.boton_contreñas = CTkButton(self.frame_lateral,text="RESTABLECER CONTRASEÑA",fg_color="blue2",command=self.Restablecer_Contraseña)
        self.boton_contreñas.place(x=40,y=130)

        self.boton_agregar = CTkButton(self.frame_lateral,text="SOLICITAR MEDICAMENTO",fg_color="blue2",width=185)
        self.boton_agregar.place(x=40,y=160)

        self.boton_actualizar = CTkButton(self.frame_lateral,text="ACTUALIZAR DATOS",fg_color="blue2",width=185)
        self.boton_actualizar.place(x=40,y=190)

        self.boton_salir = CTkButton(self.frame_lateral,text="SALIR",fg_color="blue2",width=185,command=self.Salir)
        self.boton_salir.place(x=40,y=320)
        
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

    def Restablecer_Contraseña(self):

        def Generar_Contraseña():
            bd = BaseDeDatos(host="localhost",user="root",password="Soydeboca66",database="Farmacia")
            bd.CrearConexion()
            dni = entry_dni.get()
            longitud = 6
            caracteres = "abcdefghijklmnñopqrstuvwxyzABCDEFGHIJKLMNÑOPQRSTUVWXYZ0123456789"
            lista_caracteres = list(caracteres)
            clave = ""

            i = 0
            while i < longitud:
                clave = clave + random.choice(lista_caracteres)
                i = i + 1
            
            clave_cifrada = Cifrar_Contraseña(clave)
            try:
                query = "UPDATE Usuarios u JOIN Clientes c ON c.id_usuario = u.id_usuario SET u.Contraseña = %s WHERE c.DNI = %s;"
                resultados = bd.Insertar_Datos(query,(clave_cifrada,dni))
                if resultados:    
                    messagebox.showinfo("Restablecer Contraseña","Contraseña generada exitosamente")
                    messagebox.showinfo("Restablecer Contraseña",f"Su contraseña es {clave}")
                    entry_dni.delete(0,END)
                else:
                    messagebox.showwarning("Restablecer Contraseña","Error DNI inexistente")
            except Exception as err:
                messagebox.showerror("Error interno al actualizar los datos")
                print(err)
            finally:
                bd.CerrarConexion()
            
        self.root.withdraw()
        vtn_contraseña = CTkToplevel()
        vtn_contraseña.title("Restablecer Contraseña")
        vtn_contraseña.geometry("400x350")
        vtn_contraseña.resizable(0,0)

        frame_titulo = Frame(vtn_contraseña,bg="blue2",width=400,height=100)
        frame_titulo.place(x=0)

        label_titulo = CTkLabel(frame_titulo,text="Restablecer Contraseña",fg_color="blue2",font=("Arial",25,"bold"))
        label_titulo.place(x=60,y=30)

        entry_dni = CTkEntry(vtn_contraseña,width=200,height=40,
                                       font=("Arial",16),
                                       placeholder_text="DNI",
                                       placeholder_text_color="gray",border_color="blue2")
        entry_dni.place(x=100,y=120)

        boton_restablecer = CTkButton(vtn_contraseña,text="Restablecer",fg_color="blue2",text_color="white",height=40,width=200,font=("Arial",14),command=Generar_Contraseña)
        boton_restablecer.place(x=100,y=170)

        boton_atras = CTkButton(vtn_contraseña,text="Atrás",fg_color="blue2",text_color="white",height=40,width=200,font=("Arial",14),command=lambda: self.Retroceder(vtn_contraseña))
        boton_atras.place(x=100,y=215)


    def Limpiar_Tabla(self):
        self.tabla.delete(*self.tabla.get_children())

    def Retroceder(self,ventana):
        ventana.destroy()
        self.root.deiconify()


    def Salir(self):
        self.root.destroy()