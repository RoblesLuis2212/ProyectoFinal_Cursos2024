from customtkinter import *
from tkinter import *
from tkinter import messagebox
from ConexionBD import BaseDeDatos
from tkinter import ttk
from PIL import Image,ImageTk


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

        self.boton_usuario = Button(self.root,text="Usuarios",font=("Arial",10))
        self.boton_usuario.config(image=imagen_tk,compound=LEFT,padx=50)
        self.boton_usuario.image = imagen_tk
        self.boton_usuario.place(x=130,y=200,width=290,height=50)

        self.boton_stock = Button(self.root,text="ABM Productos")
        self.boton_stock.config(image=imagen_tkStock,compound=LEFT,padx=20)
        self.boton_stock.image = imagen_tkStock
        self.boton_stock.place(x=130,y=250,width=290,height=50)
