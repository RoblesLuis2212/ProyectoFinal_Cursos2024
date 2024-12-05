from customtkinter import *
from tkinter import *
from tkinter import messagebox
from ConexionBD import BaseDeDatos

class Ventana_Registro:
    def __init__(self,root,vtn_secundaria):
        self.root =  root
        self.root.title("Ventana Registro")
        self.root.geometry("400x600")

        self.vtn_secundaria = vtn_secundaria

        set_appearance_mode("dark")
        set_default_color_theme("blue")

        self.label_titulo = CTkLabel(self.root, text="Registro",font=("Arial",30),text_color="white")
        self.label_titulo.place(x=140,y=40)

        self.entry_nombre = CTkEntry(self.root, width=200,height=40,
                                         font=("Arial",16),
                                         placeholder_text="Nombre",
                                         placeholder_text_color="gray")
        self.entry_nombre.place(x=100,y=100)

        self.entry_apellido = CTkEntry(self.root, width=200,height=40,
                                       font=("Arial",16),
                                       placeholder_text="Apellido",
                                       placeholder_text_color="gray")
        
        self.entry_apellido.place(x=100,y=160)
        
        self.entry_DNI = CTkEntry(self.root, width=200,height=40,
                                  font=("Arial",16),
                                  placeholder_text="DNI",
                                  placeholder_text_color="gray")
        self.entry_DNI.place(x=100,y=220)

        self.entry_direccion = CTkEntry(self.root, width=200,height=40,
                                        font=("Arial",16),
                                        placeholder_text="Direccion",
                                        placeholder_text_color="grey")
        
        self.entry_direccion.place(x=100,y=280)

        self.entry_contraseña = CTkEntry(self.root, width=200,height=40,
                                         font=("Arial",16),
                                         placeholder_text="Contraseña",
                                         placeholder_text_color="grey")
        
        self.entry_contraseña.place(x=100,y=340)

        self.boton_registro = CTkButton(self.root, text="Registrarse",height=40,font=("Segoe UI",14),command=self.Registrar_Cliente)
        self.boton_registro.place(x=130,y=400)


    def Registrar_Cliente(self):
        nombre = self.entry_nombre.get()
        apellido = self.entry_apellido.get()
        DNI = self.entry_DNI.get()
        direccion = self.entry_direccion.get()
        contraseña = self.entry_contraseña.get()

        username = nombre + apellido

        bd = BaseDeDatos(host="localhost",user="root",password="Soydeboca66",database="Farmacia")

        try:

            bd.CrearConexion()

            if not nombre or not apellido or not DNI or not direccion or not contraseña:
                messagebox.showwarning("Advertencia","Por favor complete todos los campos")
            
            query = "INSERT INTO Clientes (Nombre,Apellido,Direccion,DNI,Username,Contraseña) VALUES (%s,%s,%s,%s,%s,%s)"

            bd.Insertar_Datos(query,(nombre,apellido,direccion,DNI,username,contraseña))
            messagebox.showinfo("Registro","Registro Realizado Correctamente")
        
        except Exception as e:
            messagebox.showerror("Error","Error interno al registrar el usuario")
        
        finally:
            bd.CerrarConexion()
