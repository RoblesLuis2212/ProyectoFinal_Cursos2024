from customtkinter import *
from tkinter import *
from tkinter import messagebox
from PIL import Image,ImageTk

class Ventana_Clientes:
    def __init__(self,root,vtn_clientes):
        self.root = root
        self.root.title("Ventana Clientes")
        self.root.geometry("800x500")
        self.root.resizable(0,0)

        self.vtn_clientes = vtn_clientes
        
        set_appearance_mode("system")
        set_default_color_theme("green")

        self.label_titulo = CTkLabel(self.root,text="Bienvenidos Clientes",font=("Arial",30),text_color="white")
        self.label_titulo.place(x=140,y=100)

        self.frame = CTkFrame(self.root,bg_color="red")
        self.frame.place(x=100,y=100)

        imagen = Image.open("C:\\Users\\Luis Robles\\Desktop\\ProyectoFinal_Cursos2024\\ImageMedicamentos\\tafirol.jpg")
        imagen = imagen.resize((200,200))
        self.imagen_tk = ImageTk.PhotoImage(imagen)

        self.label_imagen = CTkLabel(self.frame, image=self.imagen_tk)
        self.label_imagen.pack(padx=0,pady=0)