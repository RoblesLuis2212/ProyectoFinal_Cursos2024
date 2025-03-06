from customtkinter import *
from tkinter import *
from tkinter import messagebox
from tkinter import ttk

class Ventana_Empleado:
    def __init__(self,root,rol,vtn_empleado):
        self.root = root
        self.rol = rol
        self.root.title("Ventana Empleados")
        self.root.geometry("1200x500")
        self.root.resizable(0,0)

        self.vtn_empleado = vtn_empleado

        set_appearance_mode("dark")
        set_default_color_theme("blue")

        self.label_titulo = CTkLabel(self.root,text="Ventana empleados")
        self.label_titulo.place(x=100,y=20)
