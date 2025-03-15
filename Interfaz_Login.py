from customtkinter import *
from tkinter import *
from tkinter import messagebox
from ConexionBD import BaseDeDatos
from Interfaz_Clientes import Ventana_Clientes
from PIL import Image,ImageTk
from Cifrado import *
from Interfaz_Gerente import Ventana_Gerente
from Interfaz_Empleado import Ventana_Empleado

class App:
    def __init__(self,root):
        self.root = root
        self.root.geometry("400x500")
        self.root.title("Iniciar Sesión")
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
        #Se obtienen los datos ingresados en los entry
        usuario = self.entry_username.get()
        contraseña = self.entry_contraseña.get()
        #a la contraseña ingresada es cifrada y comparada con la de la base de datos mediante la consulta
        clave_cifrada = Cifrar_Contraseña(contraseña)

        #se valida que los campos no esten vacios    
        if not usuario or not contraseña:
            messagebox.showwarning("Advertencia","Por favor complete todos los campos")
            return
            
        bd = BaseDeDatos(host="localhost",user="root",password="Soydeboca66",database="Farmacia")

        #Se crea la conexion con la base de datos
        bd.CrearConexion()
        #Se realiza un JOIN para poder obtener tanto el username,contraseña y rol 
        query = "SELECT u.Rol, c.DNI AS DNI_Cliente, e.DNI AS DNI_Empleado FROM Usuarios u LEFT JOIN Clientes c ON u.id_usuario = c.id_usuario LEFT JOIN Empleados e ON u.id_usuario = e.id_usuario WHERE u.Username = %s AND u.Contraseña = %s;"
        resultados = bd.ObtenerDatos(query,(usuario,clave_cifrada))

        #Dependiendo del rol obtenido de la base de datos se muestra la ventana correspondiente            
        if resultados:
            rol = resultados[0][0]
            dni_cliente = resultados[0][1]
            dni_empleado = resultados[0][2]
            if rol == 1:
                messagebox.showinfo("Inicio De Sesion","Inicio de sesión exitoso")
                self.Mostrar_Menu_Clientes(dni_cliente)
            elif rol == 2:    
                messagebox.showinfo("Inicio De Sesion","Inicio de sesión exitoso")
                self.Mostrar_Menu_Empleado(rol,dni_empleado)
            elif rol == 3:
                messagebox.showinfo("Inicio De Sesion","Inicio de sesión exitoso")
                self.Mostrar_Menu_Gerente(rol)
        else:
            messagebox.showwarning("Advertencia","Error usuario o contraseña incorrectos")
            
        bd.CerrarConexion()
    
    #Metodo para ocultar ventanas
    def Mostrar_Ventana(self):
        from Interfaz_Registro import Ventana_Registro 
        self.root.withdraw()

        segunda_ventana = CTkToplevel(self.root)
        Ventana_Registro(segunda_ventana, self.root)
    
    #Muestra el menu correspondiente a los clientes (se ve en el nombre del metodo no hace falta comentarlo)
    def Mostrar_Menu_Clientes(self,dni_cliente):
        self.root.withdraw()
        ventana_clientes = CTkToplevel(self.root)
        Ventana_Clientes(ventana_clientes, self.root,dni_cliente)
    
    def Mostrar_Menu_Gerente(self,rol):
        self.root.withdraw()
        ventana_gerente = CTkToplevel(self.root)
        Ventana_Gerente(ventana_gerente,self.root,rol)
    
    def Mostrar_Menu_Empleado(self,rol,dni_empleado):
        self.root.withdraw()
        ventana_empleados = CTkToplevel(self.root)
        Ventana_Empleado(ventana_empleados,rol,self.root,dni_empleado)