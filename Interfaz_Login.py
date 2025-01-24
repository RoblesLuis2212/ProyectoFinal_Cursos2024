from customtkinter import *
from tkinter import *
from tkinter import messagebox
from ConexionBD import BaseDeDatos
from Interfaz_Clientes import Ventana_Clientes
from PIL import Image,ImageTk


class App:
    def __init__(self,root):
        self.root = root
        self.root.geometry("400x500")
        self.root.title("Prototipo Proyecto")
        self.root.resizable(0,0)   
        
        set_appearance_mode("dark")
        set_default_color_theme("blue")
        
        self.label_login = CTkLabel(self.root, text="Iniciar Sesión",font=("Arial",30))
        self.label_login.place(x=120,y=50)
        
        self.entry_username = CTkEntry(self.root, width=200,height=40,
                                       font=("Arial",16),
                                       placeholder_text="Username",
                                       placeholder_text_color="gray",border_color="blue2")
        self.entry_username.place(x=110,y=150)
        
        self.entry_contraseña = CTkEntry(self.root, width=200,height=40,
                                         font=("Arial",16),
                                         placeholder_text="Contraseña",
                                         placeholder_text_color="gray",
                                         show="*",border_color="blue")
        self.entry_contraseña.place(x=110,y=200)
        
        self.boton_iniciar = CTkButton(self.root, text="Iniciar Sesión",height=40,font=("Segoe UI",14),command=self.ValidarDatos,fg_color="blue2")
        self.boton_iniciar.place(x=140,y=250)
        
        self.boton_registrarse = CTkButton(self.root, text="Registrarse",height=40,font=("Segoe UI",14),command=self.Mostrar_Ventana,fg_color="blue2")
        self.boton_registrarse.place(x=140,y=300)
    
    #Esta funcion validara los datos del formulario para poder iniciar sesion
    def ValidarDatos(self):
        usuario = self.entry_username.get()
        contraseña = self.entry_contraseña.get()
            
        if not usuario or not contraseña:
            messagebox.showwarning("Advertencia","Por favor complete todos los campos")
            
        bd = BaseDeDatos(host="localhost",user="root",password="Soydeboca66",database="Farmacia")
            
        bd.CrearConexion()
        query = "SELECT * FROM Clientes WHERE Username = %s AND Contraseña = %s"
        
        resultados = bd.ObtenerDatos(query,(usuario,contraseña))
            
        if resultados:
            messagebox.showinfo("Inicio De Sesion","Inicio de sesión exitoso")
            self.Mostrar_Menu_Clientes()
        else:
            messagebox.showwarning("Advertencia","Error usuario o contraseña incorrectos")
            
            bd.CerrarConexion()
    
    def Mostrar_Ventana(self):
        from Interfaz_Registro import Ventana_Registro 
        self.root.withdraw()

        segunda_ventana = CTkToplevel(self.root)
        Ventana_Registro(segunda_ventana, self.root)
    
    def Mostrar_Menu_Clientes(self):
        self.root.withdraw()
        ventana_clientes = CTkToplevel(self.root)
        Ventana_Clientes(ventana_clientes, self.root)


        