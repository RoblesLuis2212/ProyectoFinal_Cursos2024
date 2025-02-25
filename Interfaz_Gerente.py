from customtkinter import *
from tkinter import *
from tkinter import messagebox
from ConexionBD import BaseDeDatos
from tkinter import ttk
from PIL import Image,ImageTk
from Interfaz_Login import Ventana_Clientes
from tkinter import ttk
from Cifrado import *

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

        self.boton_usuario = Button(self.root,text="Usuarios",font=("Arial",10),command=self.Ventana_Usuarios)
        self.boton_usuario.config(image=imagen_tk,compound=LEFT,padx=50)
        self.boton_usuario.image = imagen_tk
        self.boton_usuario.place(x=100,y=120,width=320,height=70)

        self.boton_stock = Button(self.root,text="ABM Productos",command=self.Ventana_ABM_Productos)
        self.boton_stock.config(image=imagen_tkStock,compound=LEFT,padx=20)
        self.boton_stock.image = imagen_tkStock
        self.boton_stock.place(x=100,y=190,width=320,height=70)


        self.boton_empleados = Button(self.root,text="ABM Empleados",command=self.Ventana_ABM_Empleados)
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
                                       placeholder_text="DNI",
                                       placeholder_text_color="gray",border_color="blue2")
        entry_usuario.place(x=100,y=150)

        boton_contraseña = CTkButton(ventana_RC,text="Generar Contraseña",fg_color="blue2",text_color="white",height=40,width=200,font=("Arial",14))
        boton_contraseña.place(x=100,y=200)

        boton_atras = CTkButton(ventana_RC,text="Atrás",fg_color="blue2",text_color="white",height=40,width=200,font=("Arial",14),command=Retroceder)
        boton_atras.place(x=100,y=245)
    
    #Ventana para implementar el ABM del productos
    def Ventana_ABM_Productos(self):
        def Limpiar_Campos():
            entry_nombre.delete(0,END)
            entry_descripcion.delete(0,END)
            entry_precio.delete(0,END)
            entry_categoria.delete(0,END)

        def Llenar_Campos(event):
            Limpiar_Campos()
            seleccion = tabla.focus()
            print(seleccion)

            if seleccion:
                valores = tabla.item(seleccion,"values")
                print(valores)

                for fila in valores:
                    print(fila)

                entry_nombre.insert(0,valores[0])
                entry_descripcion.insert(0,valores[1])
                entry_precio.insert(0,valores[2])
                entry_categoria.insert(0,valores[3])
            
        def Retroceder():
            self.root.deiconify()
            ventana_ABM_Productos.destroy()
        
        def Actualizar_Tabla():
            for i in tabla.get_children():
                tabla.delete(i)
            
            bd.CrearConexion()
            query = "SELECT Nombre,Descripcion,Precio,Categoria FROM Medicamentos"
            resultados = bd.ObtenerDatos(query,())

            if resultados:
                for resultado in resultados:
                    tabla.insert("","end",values=resultado)
            else:
                print("Datos no encontrados en la tabla")
        
        def Cargar_Medicamento():
            bd.CrearConexion()

            nombre = entry_nombre.get()
            descripcion = entry_descripcion.get()
            precio = entry_precio.get()
            categoria = entry_categoria.get()

            try:
                query = "INSERT INTO Medicamentos (Nombre,Descripcion,Precio,Categoria) VALUES (%s,%s,%s,%s)"
                bd.Insertar_Datos(query,(nombre,descripcion,precio,categoria))
                messagebox.showinfo("Informacion","Medicamento cargado correctamente")
                Actualizar_Tabla()
                Limpiar_Campos()
                bd.CerrarConexion()
            except Exception as err:
                messagebox.showerror("Error","Error interno al cargar los datos")
                print(err)
        
        def Modificar_Medicamento():
            seleccion = tabla.focus()

            if seleccion:
                messagebox.showwarning("Advertencia","Por favor seleccione un medicamento")
                return
            
            query = "UPDATE Medicamentos SET Nombre = %s,Descripcion = %s,Precio = %s,Categoria = %s WHERE id_medicamento = %s"
        

        def Eliminar_Medicamento():
            nombre = entry_nombre.get()
            seleccion = tabla.focus()

            if not seleccion:
                messagebox.showwarning("Advertencia","Por favor seleccione el medicamento a eliminar")
                return
            
            try:
                query = "DELETE FROM Medicamentos WHERE Nombre = %s"
                bd.Insertar_Datos(query,(nombre,))
                messagebox.showinfo("Informacion","Medicamento eliminado correctamente")
                Limpiar_Campos()
                Actualizar_Tabla()
            except Exception as err:
                messagebox.showerror("Error","Error interno al eliminar los datos")
                print(err)

        self.root.withdraw()
        ventana_ABM_Productos = CTkToplevel()
        ventana_ABM_Productos.title("ABM Productos")
        ventana_ABM_Productos.geometry("800x500")
        ventana_ABM_Productos.resizable(0,0)


        frame_titulo = CTkFrame(ventana_ABM_Productos,fg_color="navy",width=250,height=500)
        frame_titulo.place(x=0)

        titulo = CTkLabel(frame_titulo,text="Agregar Nuevos Productos",font=("Lato",20))
        titulo.place(x=10,y=5)

        label_nombre = CTkLabel(frame_titulo,text="NOMBRE",font=("Rod",15,"bold"))
        label_nombre.place(x=20,y=40)
        
        entry_nombre = Entry(frame_titulo)
        entry_nombre.place(x=100,y=40)

        label_descripcion = CTkLabel(frame_titulo,text="Descripcion",font=("Rod",15,"bold"))
        label_descripcion.place(x=10,y=75)

        entry_descripcion = Entry(frame_titulo)
        entry_descripcion.place(x=100,y=80)

        label_precio = CTkLabel(frame_titulo,text="Precio",font=("Rod",15,"bold"))
        label_precio.place(x=20,y=115)

        entry_precio = Entry(frame_titulo)
        entry_precio.place(x=100,y=115)

        label_categoria = CTkLabel(frame_titulo,text="Categoria",font=("Rod",15,"bold"))
        label_categoria.place(x=10,y=150)

        entry_categoria = Entry(frame_titulo)
        entry_categoria.place(x=100,y=155)

        boton_agregar = Button(frame_titulo,text="Agregar",background="red",font="black",command=Cargar_Medicamento)
        boton_agregar.place(x=10,y=200)

        boton_modificar = Button(frame_titulo,text="Modificar",background="yellow",font="black",command=Modificar_Medicamento)
        boton_modificar.place(x=90,y=200)

        boton_eliminar = Button(frame_titulo,text="Eliminar",background="green2",font="black",command=Eliminar_Medicamento)
        boton_eliminar.place(x=180,y=200)
        

        boton_salir = Button(frame_titulo,text="Volver al menú principal",background="orange",font="black",command=Retroceder)
        boton_salir.place(x=40,y=380)

        #Creacion de la tabla para visualizar los datos
        columnas = ("Nombre","Descripcion","Precio","Categoria")
        tabla = ttk.Treeview(ventana_ABM_Productos,columns=columnas,show="headings",height=25)

        tabla.heading("Nombre",text="Nombre")
        tabla.heading("Descripcion",text="Descripcion")
        tabla.heading("Precio",text="Precio")
        tabla.heading("Categoria",text="Categoria")


        tabla.column("Nombre",width=130,anchor="center")
        tabla.column("Descripcion",width=130,anchor="center")
        tabla.column("Precio",width=130,anchor="center")
        tabla.column("Categoria",width=130,anchor="center")

        tabla.place(x=255,y=10)
        bd = BaseDeDatos(host="localhost",user="root",password="Soydeboca66",database="Farmacia")

        bd.CrearConexion()

        query = "SELECT Nombre,Descripcion,Precio,Categoria FROM Medicamentos"
        
        resultados = bd.ObtenerDatos(query,())
        if resultados:
            for resultado in resultados:
                tabla.insert("","end",values=resultado)
        else:
            print("Datos no encontrados en la tabla")
        
        tabla.bind("<<TreeviewSelect>>",Llenar_Campos)


        
    
    #Ventana donde se realiza el ABM de empleados
    def Ventana_ABM_Empleados(self):
        #Esta funcion carga los entry con los datos del empleado para que luego sean modificados
        def Llenar_Campos(event):
            Limpiar_Campos()
            seleccion = tabla.focus()
            print(seleccion)

            if seleccion:
                valores = tabla.item(seleccion,"values")
                print(valores)

                for fila in valores:
                    print(fila)

                entry_nombre.insert(0,valores[0])
                entry_apellido.insert(0,valores[1])
                entry_direccion.insert(0,valores[2])
                entry_telefono.insert(0,valores[3])
                entry_dni.insert(0,valores[4])
                entry_sueldo.insert(0,valores[5])
        #Funcion para limpiar los campos pertenecientes a la ventana
        def Limpiar_Campos():
            entry_nombre.delete(0,END)
            entry_apellido.delete(0,END)
            entry_direccion.delete(0,END)
            entry_telefono.delete(0,END)
            entry_dni.delete(0,END)
            entry_sueldo.delete(0,END)
            entry_idUsuario.delete(0,END)

        def Eliminar_Usuario():
            bd.CrearConexion()
            DNI = entry_dni.get()


            if not DNI:
                messagebox.showwarning("Advertencia","Por favor ingrese el DNI del empleado a eliminar")
                return
            
            try:
                query = "DELETE FROM Empleados WHERE DNI = %s"
                bd.Insertar_Datos(query,(DNI,))
                messagebox.showinfo("Informacion","Usuario eliminado correctamente")
                Actualizar_Tabla()
                Limpiar_Campos()
                bd.CerrarConexion()
            except Exception as err:
                messagebox.showwarning("Advertencia!","Por favor ingrese el DNI del empleado a eliminar")
                print(err)

        #Funcion para agregar usuarios a la base de datos
        def Agregar_Usuario():
            id = entry_idUsuario.get()
            nombre = entry_nombre.get()
            apellido = entry_apellido.get()
            direccion = entry_direccion.get()
            telefono = entry_telefono.get()
            dni = entry_dni.get()
            sueldo = entry_sueldo.get()


            #Se verifica mediante el try que los campos no esten vacios antes de enviarlos a la BD
            try:
                bd.CrearConexion()
                if not nombre or not apellido or not direccion or not telefono or not dni or not sueldo:
                    messagebox.showwarning("Advertencia!","Por favor complete todo los campos")
                    return #El return se utiliza para que el programa no siga avanzando en la ejecucion
            
                query = "INSERT INTO Empleados (id_usuario,Nombre,Apellido,Direccion,Telefono,DNI,Sueldo) VALUES (%s,%s,%s,%s,%s,%s,%s)"

                bd.Insertar_Datos(query,(id,nombre,apellido,direccion,telefono,dni,sueldo))
                messagebox.showinfo("Informacion","Datos cargados correctamente")
                Actualizar_Tabla()
                Limpiar_Campos()
            except Exception as e:
                messagebox.showerror("Error","Se ha producido un error al insertar los datos")
                print(e)
            finally:
                bd.CerrarConexion()
        
        def Modificar_Usuario():
            bd.CrearConexion()
            seleccion = tabla.focus()

            if not seleccion:
                messagebox.showwarning("Advertencia","Por favor seleccione una fila para modificar")
                return

            nombre = entry_nombre.get()
            apellido = entry_apellido.get()
            direccion = entry_direccion.get()
            telefono = entry_telefono.get()
            dni_empleado = entry_dni.get()
            sueldo = entry_sueldo.get()
            
            if not dni_empleado:
                    messagebox.showwarning("Advertencia","Error, ingrese un DNI valido")
                    return
            
            try:
                query = "UPDATE Empleados SET Nombre = %s,Apellido = %s,Direccion = %s,Telefono = %s,DNI = %s,Sueldo = %s WHERE DNI = %s"
                bd.Insertar_Datos(query,(nombre,apellido,direccion,telefono,dni_empleado,sueldo,dni_empleado))
                messagebox.showinfo("Informacion","Datos actualizados correctamente")
                Limpiar_Campos()
                Actualizar_Tabla()
                bd.CerrarConexion()
            
            except Exception as err:
                messagebox.showerror("Error","Error interno al actualizar los datos")
                Limpiar_Campos()

        bd = BaseDeDatos(host="localhost",user="root",password="Soydeboca66",database="Farmacia")

        #funcion para volver al menu principal
        def Retroceder():
            self.root.deiconify()
            vtn_ABM_Empleados.destroy()
        
        #Diseño correspondiente a la ventana "ABM Empleados"
        self.root.withdraw()
        vtn_ABM_Empleados = CTkToplevel()
        vtn_ABM_Empleados.title("ABM Empleados")
        vtn_ABM_Empleados.geometry("1050x500")
        vtn_ABM_Empleados.resizable(0,0)
        
        frame_titulo = CTkFrame(vtn_ABM_Empleados,fg_color="black",width=250,height=500)
        frame_titulo.place(x=0)

        titulo = CTkLabel(frame_titulo,text="Agregar Nuevos Empleados",font=("Lato",20))
        titulo.place(x=5,y=5)

        label_nombre = CTkLabel(frame_titulo,text="NOMBRE",font=("Rod",15,"bold"))
        label_nombre.place(x=20,y=40)
        
        entry_nombre = Entry(frame_titulo)
        entry_nombre.place(x=100,y=40)

        label_apellido = CTkLabel(frame_titulo,text="APELLIDO",font=("Rod",15,"bold"))
        label_apellido.place(x=20,y=75)

        entry_apellido = Entry(frame_titulo)
        entry_apellido.place(x=100,y=80)

        label_direccion = CTkLabel(frame_titulo,text="DIRECCION",font=("Rod",15,"bold"))
        label_direccion.place(x=10,y=115)

        entry_direccion = Entry(frame_titulo)
        entry_direccion.place(x=100,y=115)

        label_telefono = CTkLabel(frame_titulo,text="TELEFONO",font=("Rod",15,"bold"))
        label_telefono.place(x=10,y=150)

        entry_telefono = Entry(frame_titulo)
        entry_telefono.place(x=100,y=155)

        label_dni = CTkLabel(frame_titulo,text="DNI",font=("Rod",15,"bold"))
        label_dni.place(x=45,y=190)

        entry_dni = Entry(frame_titulo)
        entry_dni.place(x=100,y=190)
        
        label_sueldo = CTkLabel(frame_titulo,text="SUELDO",font=("Rod",15,"bold"))
        label_sueldo.place(x=20,y=230)

        entry_sueldo = Entry(frame_titulo)
        entry_sueldo.place(x=100,y=230)

        label_ID = CTkLabel(frame_titulo,text="ID USUARIO",font=("Rod",15,"bold"))
        label_ID.place(x=10,y=270)

        entry_idUsuario = Entry(frame_titulo)
        entry_idUsuario.place(x=100,y=270)

        boton_agregar = Button(frame_titulo,text="Agregar",background="red",font="black",command=Agregar_Usuario)
        boton_agregar.place(x=10,y=310)

        boton_modificar = Button(frame_titulo,text="Modificar",background="yellow",font="black",command=Modificar_Usuario)
        boton_modificar.place(x=90,y=310)

        boton_eliminar = Button(frame_titulo,text="Eliminar",background="green2",font="black",command=Eliminar_Usuario)
        boton_eliminar.place(x=180,y=310)
        
        # entry_busqueda = Entry(frame_titulo)
        # entry_busqueda.place(x=70,y=350)

        # boton_buscar = Button(frame_titulo,text="Buscar Por Nombre",background="orange",font="black")
        # boton_buscar.place(x=50,y=380)

        boton_atras = Button(frame_titulo,text="Volver al menú principal",background="orange",font="black",command=Retroceder)
        boton_atras.place(x=40,y=380)

        #Creacion de la tabla para visualizar los datos
        columnas = ("Nombre","Apellido","Direccion","Telefono","DNI","Sueldo")
        tabla = ttk.Treeview(vtn_ABM_Empleados,columns=columnas,show="headings",height=25)

        #Se definen los encabezados de las columnas de la tabla
        tabla.heading("Nombre",text="Nombre")
        tabla.heading("Apellido",text="Apellido")
        tabla.heading("Direccion",text="Direccion")
        tabla.heading("Telefono",text="Telefono")
        tabla.heading("DNI",text="DNI")
        tabla.heading("Sueldo",text="Sueldo")

        #Definicion de las columnas de la tabla, tambien se ajustan los tamaños y posiciones
        tabla.column("Nombre",width=130,anchor="center")
        tabla.column("Apellido",width=130,anchor="center")
        tabla.column("Direccion",width=130,anchor="center")
        tabla.column("Telefono",width=130,anchor="center")
        tabla.column("DNI",width=130,anchor="center")
        tabla.column("Sueldo",width=130,anchor="center")

        tabla.place(x=255,y=10)

        #Consulta para mostrar los datos en la tabla
        bd.CrearConexion()
        query = "SELECT Nombre,Apellido,Direccion,Telefono,DNI,Sueldo FROM Empleados"
        resultados = bd.ObtenerDatos(query,())

        #Apartir de los resultados obtenidos se utiliza un bucle para recorrerlos
        if resultados:
            for resultado in resultados:
                tabla.insert("","end",values=resultado)
        else:
            print("Datos no encontrados en la tabla")

        #Esta funcion actualiza los datos de la tabla inmediatamente al agregar un nuevo empleado
        def Actualizar_Tabla():
            for i in tabla.get_children():
                tabla.delete(i)
            
            bd.CrearConexion()
            query = "SELECT Nombre,Apellido,Direccion,Telefono,DNI,Sueldo FROM Empleados"
            resultados = bd.ObtenerDatos(query,())

            if resultados:
                for resultado in resultados:
                    tabla.insert("","end",values=resultado)
            else:
                print("Datos no encontrados en la tabla")
        
        tabla.bind("<<TreeviewSelect>>",Llenar_Campos)

    #ventana para el registro de usuarios (empleados)   
    def Ventana_Usuarios(self):
        #Funcion para registrar los uevos empleados
        def Registrar_Usuarios():
            username = entry_username.get()
            contraseña = entry_contraseña.get()

            contraseña_cifrada = Cifrar_Contraseña(contraseña)

            bd = BaseDeDatos(host="localhost",user="root",password="Soydeboca66",database="Farmacia")

            try:
                bd.CrearConexion()
                if not username or not contraseña:
                    messagebox.showwarning("Advertencia","Por favor complete todos los campos")
                    return
                
                query = "INSERT INTO Usuarios (Username,Contraseña,Rol) VALUES (%s,%s,%s)"
                rol = 2

                bd.Insertar_Datos(query,(username,contraseña_cifrada,rol))
                messagebox.showinfo("Informacion","usuario registrado correctamente")

                id_usuario = bd.Obtener_Id_Usuario()

                messagebox.showinfo("Informacion",f"Su ID de usuario es: {id_usuario}")

                #Se limpian los campos al registrar correctamente los datos
                entry_username.delete(0,END)
                entry_contraseña.delete(0,END)
            
            #Capturador de errores
            except Exception as e:
                messagebox.showerror("Error","Se ha producido un error al registar el usuario")
                print(e)

        #Funcion de retroceder correspondiente a esta ventana
        def Retroceder():
            self.root.deiconify()
            vtn_usuario.destroy()

        self.root.withdraw()

        #Diseño de la ventana "Usuarios"
        vtn_usuario = CTkToplevel()
        vtn_usuario.title("Usuarios")
        vtn_usuario.geometry("400x500")
        vtn_usuario.resizable(0,0)

        frame_titulo = CTkFrame(vtn_usuario,fg_color="blue",width=400,height=80)
        frame_titulo.place(x=0)

        label_titulo = CTkLabel(frame_titulo,text="Registro de datos",font=("verdana",25,"bold"))
        label_titulo.place(x=80,y=20)

        entry_username = CTkEntry(vtn_usuario,width=200,height=40,
                                       font=("Arial",16),
                                       placeholder_text="Username",
                                       placeholder_text_color="gray",border_color="blue2")
        entry_username.place(x=100,y=120)

        entry_contraseña = CTkEntry(vtn_usuario,width=200,height=40,
                                       font=("Arial",16),
                                       placeholder_text="Contraseña",
                                       placeholder_text_color="gray",border_color="blue2")
        entry_contraseña.place(x=100,y=170)

        boton_registrar = CTkButton(vtn_usuario,text="registrar",fg_color="blue",width=200,height=40,font=("arial",15,"bold"),command=Registrar_Usuarios)
        boton_registrar.place(x=100,y=220)

        boton_atras = CTkButton(vtn_usuario,text="Atrás",fg_color="blue",width=200,height=40,font=("arial",15,"bold"),command=Retroceder)
        boton_atras.place(x=100,y=270)

    def Salir(self):
        opcion = messagebox.askokcancel("Salir","¿Esta seguro de que desea salir?")
        if opcion:
            self.root.destroy()