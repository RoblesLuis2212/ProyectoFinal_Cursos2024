from customtkinter import *
from tkinter import *
from tkinter import messagebox
from ConexionBD import BaseDeDatos
from Interfaz_Login import App
from Cifrado import *

class Ventana_Registro:
    def __init__(self,root,vtn_secundaria):
        self.root =  root
        self.root.title("Ventana Registro")
        self.root.geometry("400x600")
        self.root.resizable(0,0)

        self.vtn_secundaria = vtn_secundaria

        set_appearance_mode("dark")
        set_default_color_theme("blue")

        self.label_titulo = CTkLabel(self.root, text="Registro",font=("Arial",30),text_color="white")
        self.label_titulo.place(x=140,y=40)

        self.entry_nombre = CTkEntry(self.root, width=200,height=40,
                                         font=("Arial",16),
                                         placeholder_text="Nombre",
                                         placeholder_text_color="gray",border_color="blue2")
        self.entry_nombre.place(x=100,y=100)

        self.entry_apellido = CTkEntry(self.root, width=200,height=40,
                                       font=("Arial",16),
                                       placeholder_text="Apellido",
                                       placeholder_text_color="gray",border_color="blue2")
        
        self.entry_apellido.place(x=100,y=150)
        
        self.entry_DNI = CTkEntry(self.root, width=200,height=40,
                                  font=("Arial",16),
                                  placeholder_text="DNI",
                                  placeholder_text_color="gray",border_color="blue2")
        self.entry_DNI.place(x=100,y=200)

        self.entry_direccion = CTkEntry(self.root, width=200,height=40,
                                        font=("Arial",16),
                                        placeholder_text="Direccion",
                                        placeholder_text_color="grey",border_color="blue2")
        
        self.entry_direccion.place(x=100,y=250)

        self.entry_telefono = CTkEntry(self.root,width=200,height=40,
                                       font=("Arial",16),
                                        placeholder_text="Telefono",
                                        placeholder_text_color="grey",border_color="blue2")
        
        self.entry_telefono.place(x=100,y=300)

        opciones = ["RED DE SEGURO MEDICO","SANCOR SALUD","PAMI","OSMEDICA","NINGUNA"]
        self.list_obrasocial = CTkOptionMenu(root,values=opciones,width=200,height=35,fg_color="blue2")

        self.list_obrasocial.place(x=100,y=400)

        self.list_obrasocial.set("Seleccionar Obra Social")
        
        self.entry_contraseña = CTkEntry(self.root, width=200,height=40,
                                         font=("Arial",16),
                                         placeholder_text="Contraseña",
                                         placeholder_text_color="grey",border_color="blue2")
        
        self.entry_contraseña.place(x=100,y=350)

        self.boton_registro = CTkButton(self.root, text="Registrarse",height=40,font=("Segoe UI",14),command=self.Registrar_Cliente,fg_color="blue2")
        self.boton_registro.place(x=130,y=445)

        self.boton_atras = CTkButton(self.root,text="Atrás",height=40,font=("Segoe UI",14),command=self.Retroceder_Ventana,fg_color="blue2")
        self.boton_atras.place(x=130,y=490)


    def Registrar_Cliente(self):
        nombre = self.entry_nombre.get()
        apellido = self.entry_apellido.get()
        DNI = self.entry_DNI.get()
        telefono = self.entry_telefono.get()
        obra_social = self.list_obrasocial.get()
        direccion = self.entry_direccion.get()
        contraseña = self.entry_contraseña.get()

        contraseña_cifrada = Cifrar_Contraseña(contraseña)

        username = nombre + apellido

        lista_datos = [nombre,apellido,DNI,telefono,obra_social,direccion,contraseña]

        bd = BaseDeDatos(host="localhost",user="root",password="Soydeboca66",database="Farmacia")

        try:

            bd.CrearConexion()

            if not nombre or not apellido or not DNI or not direccion or not telefono or not contraseña:
                messagebox.showwarning("Advertencia","Por favor complete todos los campos")
                return
            
            #Habilitar linea para verificacion de datos correctos
            
            # for i in lista_datos:
            #     if len(i) < 3:
            #         messagebox.showwarning("Advertencia","Por favor ingrese datos validos")
            #         return
            
            query = "INSERT INTO Clientes (Nombre,Apellido,Direccion,Telefono,DNI,Obra_Social,Username,Contraseña) VALUES (%s,%s,%s,%s,%s,%s,%s,%s)"

            bd.Insertar_Datos(query,(nombre,apellido,direccion,telefono,DNI,obra_social,username,contraseña_cifrada))
            messagebox.showinfo("Registro",f"Registro Realizado Correctamente \nsu username es: {username}")
            self.Limpiar_Campos()
            self.Retroceder_Ventana()

        
        except Exception as e:
            messagebox.showerror("Error","Error interno al registrar el usuario ",e)
        
        finally:
            bd.CerrarConexion()
    
    def Retroceder_Ventana(self):
        self.root.withdraw()
        self.vtn_secundaria.deiconify()
        self.root.destroy()
    
    def Limpiar_Campos(self):
        self.entry_nombre.delete(0,END)
        self.entry_apellido.delete(0,END)
        self.entry_DNI.delete(0,END)
        self.entry_direccion.delete(0,END)
        self.entry_telefono.delete(0,END)
        self.entry_contraseña.delete(0,END)

        self.list_obrasocial.set("Seleccionar Obra Social")
        
