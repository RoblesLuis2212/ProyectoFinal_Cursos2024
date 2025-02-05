from customtkinter import *
from tkinter import *
from tkinter import messagebox
from ConexionBD import BaseDeDatos
from tkinter import ttk
from PIL import Image,ImageTk
from Interfaz_Login import Ventana_Clientes

class Ventana_Gerente:
    def __init__(self,root,rol,vtn_gerente):
        self.root = root
        self.rol = rol
        self.root.title("Ventana Gerente")
        self.root.geometry("500x600")
        self.root.resizable(0,0)


        self.vtn_gerente = vtn_gerente

        self.frame_title = CTkFrame(self.root,fg_color="blue",width=500,height=80)
        self.frame_title.place(x=0)

        self.label_titulo = CTkLabel(self.frame_title,text="GERENTE",text_color="white",font=("verdana",30))
        self.label_titulo.place(x=180,y=20)

        imagen_pil = Image.open("C:\\Users\\Luis Robles\\Desktop\\ProyectoFinal_Cursos2024\\usuario-multiple.png")

        imagen_resize = imagen_pil.resize((50,50))
        imagen_tk = ImageTk.PhotoImage(imagen_resize)

        imagen_stock = Image.open("C:\\Users\\Luis Robles\\Desktop\\ProyectoFinal_Cursos2024\\carro.png")
        imagen_stockR = imagen_stock.resize((40,40))
        imagen_tkStock = ImageTk.PhotoImage(imagen_stockR)
        
        imagen_empleados = Image.open("C:\\Users\\Luis Robles\\Desktop\\ProyectoFinal_Cursos2024\\trabajo-en-equipo.png")
        imagen_empleadosR = imagen_empleados.resize((60,60))
        imagen_empleadosTk = ImageTk.PhotoImage(imagen_empleadosR)

        imagen_claves = Image.open("C:\\Users\\Luis Robles\\Desktop\\ProyectoFinal_Cursos2024\\candado.png")
        imagen_clavesR = imagen_claves.resize((40,40))
        imagen_clavesTK = ImageTk.PhotoImage(imagen_clavesR)


        imagen_presupuesto = Image.open("C:\\Users\\Luis Robles\\Desktop\\ProyectoFinal_Cursos2024\\svg.png")
        imagen_presupuestoR = imagen_presupuesto.resize((40,40))
        imagen_presupuestoTK = ImageTk.PhotoImage(imagen_presupuestoR)

        imagen_salir = Image.open("C:\\Users\\Luis Robles\\Desktop\\ProyectoFinal_Cursos2024\\salida-de-emergencia.png")
        imagen_salirR = imagen_salir.resize((40,40))
        imagen_salirTK = ImageTk.PhotoImage(imagen_salirR)

        self.boton_usuario = Button(self.root,text="Usuarios",font=("Arial",10))
        self.boton_usuario.config(image=imagen_tk,compound=LEFT,padx=50)
        self.boton_usuario.image = imagen_tk
        self.boton_usuario.place(x=100,y=120,width=320,height=70)

        self.boton_stock = Button(self.root,text="ABM Productos")
        self.boton_stock.config(image=imagen_tkStock,compound=LEFT,padx=20)
        self.boton_stock.image = imagen_tkStock
        self.boton_stock.place(x=100,y=190,width=320,height=70)


        self.boton_empleados = Button(self.root,text="ABM Empleados")
        self.boton_empleados.config(image=imagen_empleadosTk,compound=LEFT,padx=15)
        self.boton_empleados.image = imagen_empleadosTk
        self.boton_empleados.place(x=100,y=260,width=320,height=70)

        self.boton_contraseñas = Button(self.root,text="Restablecer Contraseñas",command=self.Ventana_Contraseñas)
        self.boton_contraseñas.config(image=imagen_clavesTK,compound=LEFT,padx=5)
        self.boton_contraseñas.image = imagen_clavesTK
        self.boton_contraseñas.place(x=100,y=330,width=320,height=70)

        self.boton_presupuesto = Button(self.root,text="Visualizar Presupuesto")
        self.boton_presupuesto.config(image=imagen_presupuestoTK,compound=LEFT,padx=15)
        self.boton_presupuesto.image = imagen_presupuestoTK
        self.boton_presupuesto.place(x=100,y=400,width=320,height=70)

        self.boton_salir = Button(self.root,text="Salir",command=self.Salir)
        self.boton_salir.config(image=imagen_salirTK,compound=LEFT,padx=80)
        self.boton_salir.image = imagen_salirTK
        self.boton_salir.place(x=100,y=470,width=320,height=70)



    #Esta es la ventana para restablacer las contraseñas
    def Ventana_Contraseñas(self):

        def Retroceder():
            self.root.deiconify()
            ventana_RC.destroy()

        #Creacion de la ventana
        self.root.withdraw()
        ventana_RC = CTkToplevel()
        ventana_RC.title("Restablecer Contraseñas")
        ventana_RC.geometry("400x350")
        ventana_RC.resizable(0,0)

        frame = CTkFrame(ventana_RC,fg_color="blue",width=400,height=100)
        frame.place(x=0)

        label_titulo = CTkLabel(ventana_RC,text="Contraseñas",fg_color="blue",text_color="white",font=("verdana",35))
        label_titulo.place(x=100,y=30)

        entry_usuario = CTkEntry(ventana_RC,width=200,height=40,
                                       font=("Arial",16),
                                       placeholder_text="username",
                                       placeholder_text_color="gray",border_color="blue2")
        entry_usuario.place(x=100,y=150)

        boton_contraseña = CTkButton(ventana_RC,text="Generar Contraseña",fg_color="blue2",text_color="white",height=40,width=200,font=("Arial",14))
        boton_contraseña.place(x=100,y=200)

        boton_atras = CTkButton(ventana_RC,text="Atrás",fg_color="blue2",text_color="white",height=40,width=200,font=("Arial",14),command=Retroceder)
        boton_atras.place(x=100,y=245)


    def Salir(self):
        opcion = messagebox.askokcancel("Salir","¿Esta seguro de que desea salir?")
        if opcion:
            self.root.destroy()