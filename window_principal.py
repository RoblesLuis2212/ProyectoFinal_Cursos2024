from customtkinter import *
from tkinter import *
from tkinter import messagebox



class App:
    def __init__(self,root):
        self.root = root
        self.root.title("Ventana Principal")
        self.root.geometry("600x400")

        set_appearance_mode("dark")
        set_default_color_theme("blue")

        self.label_prueba = CTkLabel(self.root, text="Titulo",font=("Arial",30))
        self.label_prueba.place(x=120,y=50)

        self.boton_windows = CTkButton(self.root, text="Abrir",font=("Arial",18),
                                       text_color="white",
                                       width=150,height=40,
                                       command=self.Abrir_Ventana)
        self.boton_windows.place(x=200,y=200)
    

    def Abrir_Ventana(self):
        self.root.withdraw()

        segunda_vtn = CTkToplevel(self.root)
        Segunda_Ventana(segunda_vtn, self.root)

class Segunda_Ventana:
    def __init__(self,root,vtn_principal):
        self.root = root
        self.root.title("Ventana Secundaria")
        self.root.geometry("600x400")

        self.vtn_principal = vtn_principal

        self.label = CTkLabel(self.root, text="Bienvenido a la ventana secundaria!",font=("Arial",30))
        self.label.place(x=120,y=50)


        self.boton_salir = CTkButton(self.root, text="SALIR",font=("Arial",30),command=self.Cerrar_Ventana)
        self.boton_salir.place(x=200,y=200)

        self.boton_volver = CTkButton(self.root,text="VOLVER",font=("Arial",30),command=self.Retroceder)
        self.boton_volver.place(x=60,y=200)

    def Cerrar_Ventana(self):
        self.root.destroy()
    

    def Retroceder(self):
        self.root.destroy()
        self.vtn_principal.deiconify()