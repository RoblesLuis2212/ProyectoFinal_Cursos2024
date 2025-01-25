from customtkinter import *
from tkinter import *
from tkinter import messagebox
from PIL import Image,ImageTk
from ConexionBD import BaseDeDatos

class Ventana_Clientes:
    def __init__(self,root,vtn_clientes,dni_cliente):
        self.root = root
        self.root.title("Ventana Clientes")
        self.root.geometry("800x500")
        self.root.resizable(0,0)

        self.vtn_clientes = vtn_clientes


        bd = BaseDeDatos(host="localhost",user="root",password="Soydeboca66",database="Farmacia")

        bd.CrearConexion()

        query = "SELECT Nombre,Apellido,DNI,Obra_Social FROM Clientes WHERE DNI = %s"
        params = (dni_cliente,)
        
        resultados = bd.ObtenerDatos(query,params)


        set_appearance_mode("system")
        set_default_color_theme("green")

        self.frame_lateral = CTkFrame(self.root,fg_color="white",height=500,width=250,corner_radius=10)
        self.frame_lateral.place(x=0)

        self.label_datos = CTkLabel(self.frame_lateral,text="Datos Cliente",text_color="black",font=("Comic Sans MS",25,"bold"))
        self.label_datos.place(x=20,y=5)

        imagen_cliente = Image.open("C:\\Users\\Luis Robles\\Desktop\\ProyectoFinal_Cursos2024\\cliente.png")
        imagen_cliente = imagen_cliente.resize((200,200))
        imagen_tk = ImageTk.PhotoImage(imagen_cliente)

        self.imagen = CTkLabel(self.frame_lateral,image=imagen_tk,text="")
        self.imagen.place(x=30,y=50)

        self.boton_salir = CTkButton(self.frame_lateral,text="SALIR",fg_color="green2",text_color="black")
        self.boton_salir.place(x=30,y=400)

        # self.nombre = CTkLabel(self.frame_lateral,text=f"Nombre: {resultados[0][0]} {resultados[0][1]}",text_color="black",font=("Comic Sans MS",15))
        # self.nombre.place(x=30,y=40)

        # self.label_DNI = CTkLabel(self.frame_lateral,text=f"DNI: {resultados[0][2]}",text_color="black",font=("Comic Sans MS",15))
        # self.label_DNI.place(x=30,y=65)

        # self.label_obrasocial = CTkLabel(self.frame_lateral,text=f"Obra Social: {resultados[0][3]}",text_color="black",font=("Comic Sans MS",15))
        # self.label_obrasocial.place(x=20,y=100)



        self.imagen.image = imagen_tk