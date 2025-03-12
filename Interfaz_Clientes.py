from customtkinter import *
from tkinter import *
from tkinter import messagebox
from PIL import Image,ImageTk
from ConexionBD import BaseDeDatos
from tkinter import ttk
import datetime
from Cifrado import Cifrar_Contraseña

class Ventana_Clientes:
    def __init__(self,root,vtn_clientes,dni_cliente):
        self.root = root
        self.dni_cliente = dni_cliente
        self.root.title("Ventana Clientes")
        self.root.geometry("1200x500")
        self.root.resizable(0,0)

        self.vtn_clientes = vtn_clientes

        bd = BaseDeDatos(host="localhost",user="root",password="Soydeboca66",database="Farmacia")

        bd.CrearConexion()

        query = "SELECT Nombre,Apellido,DNI,Obra_Social FROM Clientes WHERE DNI = %s"
        params = (dni_cliente,)
        
        resultados = bd.ObtenerDatos(query,params)


        set_appearance_mode("system")
        set_default_color_theme("green")

        self.frame_lateral = CTkFrame(self.root,fg_color="purple4",height=500,width=250,corner_radius=10)
        self.frame_lateral.place(x=0)

        self.label_datos = CTkLabel(self.frame_lateral,text="Datos Cliente",text_color="black",font=("Comic Sans MS",25,"bold"))
        self.label_datos.place(x=40,y=5)

        imagen_cliente = Image.open("C:\\Users\\Luis Robles\\Desktop\\ProyectoFinal_Cursos2024\\cliente.png")
        imagen_cliente = imagen_cliente.resize((200,200))
        imagen_tk = ImageTk.PhotoImage(imagen_cliente)

        self.imagen = CTkLabel(self.frame_lateral,image=imagen_tk,text="")
        self.imagen.place(x=30,y=50)
        
        self.nombre = CTkLabel(self.frame_lateral,text=f"Nombre: {resultados[0][0]} {resultados[0][1]}",text_color="black",font=("Comic Sans MS",15))
        self.nombre.place(x=30,y=240)

        self.label_DNI = CTkLabel(self.frame_lateral,text=f"DNI: {resultados[0][2]}",text_color="black",font=("Comic Sans MS",15))
        self.label_DNI.place(x=30,y=260)
        
        self.label_obrasocial = CTkLabel(self.frame_lateral,text=f"Obra Social: {resultados[0][3]}",text_color="black",font=("Comic Sans MS",15))
        self.label_obrasocial.place(x=30,y=280)

        self.boton_salir = CTkButton(self.frame_lateral,text="SALIR",fg_color="blue",text_color="white",font=("Arial",15),width=180,command=self.Salir_Ventana)
        self.boton_salir.place(x=30,y=420)

        self.imagen.image = imagen_tk
        columnas = ("Nombre","Descripcion","Precio","Categoria")
        self.tree = ttk.Treeview(self.root,columns=columnas,show="headings")

        self.tree.heading("Nombre",text="Nombre")
        self.tree.heading("Descripcion",text="Descripcion")
        self.tree.heading("Precio",text="Precio")
        self.tree.heading("Categoria",text="Categoría")

        self.tree.column("Nombre",width=130,anchor="center")
        self.tree.column("Descripcion",width=130,anchor="center")
        self.tree.column("Precio",width=130,anchor="center")
        self.tree.column("Categoria",width=145,anchor="center")

        self.tree.place(x=255,y=10)
        
        query = "SELECT Nombre,Descripcion,Precio,Categoria FROM Medicamentos"
        medicamentos = bd.ObtenerDatos(query,())

        for medicamento in medicamentos:
            self.tree.insert("","end",values=medicamento)

        columnas_tablaf = ("Nombre","Precio")
        self.tabla_final = ttk.Treeview(self.root,columns=columnas_tablaf,show="headings")

        self.tabla_final.heading("Nombre",text="Nombre")
        self.tabla_final.heading("Precio",text="Precio")

        self.tabla_final.column("Nombre",width=130,anchor="center")
        self.tabla_final.column("Precio",width=130,anchor="center")

        self.tabla_final.place(x=850,y=10)

        self.boton_agregar = CTkButton(self.root,text="Agregar",fg_color="blue",command=self.Agregar_Producto)
        self.boton_agregar.place(x=255,y=250)

        self.boton_eliminar = CTkButton(self.root,text="Eliminar",fg_color="blue",command=self.Eliminar_Producto)
        self.boton_eliminar.place(x=400,y=250)

        metodos_pago = ("Efectivo","Debito","Credito")
        self.lista_metodopago = CTkOptionMenu(self.root,values=metodos_pago,width=200,height=35,fg_color="blue")
        self.lista_metodopago.place(x=800,y=350)
        self.lista_metodopago.set("Seleccionar Metodo De Pago")

        
        self.label_montoFinal = CTkLabel(self.root,text=f"Monto a pagar:",text_color="white",font=("verdana",30))
        self.label_montoFinal.place(x=260,y=420)

        self.boton_finalizar = CTkButton(self.root,text="Finalizar Compra",fg_color="blue",text_color="white",width=70,height=30,command=self.Finalizar_Compra)
        self.boton_finalizar.place(x=800,y=420)

        self.boton_clave = CTkButton(self.frame_lateral,text="CAMBIAR CONTRASEÑA",fg_color="blue2",text_color="white",font=("Arial",15),command=self.Ventana_Contraseña)
        self.boton_clave.place(x=30,y=380)
        
    def Agregar_Producto(self):
        item_seleccionado = self.tree.selection()
        if item_seleccionado:
            medicamento = self.tree.item(item_seleccionado)["values"]
            self.tabla_final.insert("","end",values=(medicamento[0],medicamento[2]))
            self.Calcular_Total()
        else:
            messagebox.showwarning("Advertencia","Por favor seleccione un medicamento")
    
    def Eliminar_Producto(self):
        item = self.tabla_final.selection()
        if item:
            medicamento = self.tabla_final.item(item)["values"]
            self.tabla_final.delete(item)
            self.Calcular_Total()
        else:
            messagebox.showwarning("Advertencia","Por favor seleccione el medicamento a eliminar")
    
    def Calcular_Total(self):
        total = 0
        for item in self.tabla_final.get_children():
            precio = float(self.tabla_final.item(item)["values"][1])
            total += precio
        self.label_montoFinal.configure(text=f"Monto a pagar: {total}")
        return total
    
    def Finalizar_Compra(self):
        dni_cliente = self.dni_cliente
        total = 0
        productos_seleccionados= {}
        metodo_pago = self.lista_metodopago.get()


        for item in self.tabla_final.get_children():
            nombre_medicamento = self.tabla_final.item(item)["values"][0]
            precio = float(self.tabla_final.item(item)["values"][1])
            total += precio

            if nombre_medicamento in productos_seleccionados:
                productos_seleccionados[nombre_medicamento]["cantidad"] += 1
            else:
                productos_seleccionados[nombre_medicamento] = {
                    "cantidad" : 1,
                    "precio" : precio
                }

        if total == 0:
            messagebox.showwarning("Advertencia","No hay productos seleccionados para finalizar la compra")
            return
        
        bd = BaseDeDatos(host="localhost",user="root",password="Soydeboca66",database="Farmacia")
        bd.CrearConexion()

        
        query_id = "SELECT id_cliente FROM Clientes WHERE DNI = %s"
        id_cliente = bd.ObtenerDatos(query_id,(dni_cliente,))
        
        if id_cliente:
            id_cliente = id_cliente[0][0]
            query = "INSERT INTO Pedidos(Fecha_Pedido,Total,Estado,Metodo_Pago,id_cliente) VALUES (%s,%s,%s,%s,%s)"
            params = (datetime.date.today(),total,'Pendiente',metodo_pago,id_cliente)

            bd.Insertar_Datos(query,params)

            query_id_pedido = "SELECT LAST_INSERT_ID()"
            id_pedido = bd.ObtenerDatos(query_id_pedido,())[0][0]

        #Insertar productos en detalle pedidos con sus cantidades
        for nombre_medicamento,datos in productos_seleccionados.items():
            print(f"Medicamento: {nombre_medicamento}, Cantidad: {datos['cantidad']}")
            query_medicamento = "SELECT id_medicamento FROM Medicamentos WHERE Nombre = %s"
            id_medicamento = bd.ObtenerDatos(query_medicamento,(nombre_medicamento,))[0][0]

            #Insertar en la tabla detalle pedidos
            query_detalle = "INSERT INTO Detalle_Pedidos (Cantidad,id_pedido,id_medicamento) VALUES (%s,%s,%s)"
            params_detalle = (datos["cantidad"],id_pedido,id_medicamento)
            bd.Insertar_Datos(query_detalle,(params_detalle))
        

        messagebox.showinfo("Compra Finalizada",f"Compra finalizada con exito el monto a pagar es {total}")
        messagebox.showinfo("Compra Finalizada",f"Su codigo para retirar el pedido es: {id_pedido}")
        self.tabla_final.delete(*self.tabla_final.get_children())
        self.Calcular_Total()
    
    def Ventana_Contraseña(self):
        self.root.withdraw()

        def Retroceder():
            vtn_contraseña.destroy()
            self.root.deiconify()
        
        def Cambiar_Contraseña():
            #Se obtienen los datos de los entry
            contraseña_actual = entry_clave_actual.get()
            contraseña_nueva = entry_clave_nueva.get()
            contraseña_confirmada = entry_confirmar_clave.get()

            #Se verifica que los campos no esten vacios
            if not contraseña_actual or not contraseña_nueva or not contraseña_confirmada:
                messagebox.showwarning("Advertencia","Por favor complete todos los campos")
                return
            
            #Verifica que la contraseña nueva sea igual a la confirmada
            if contraseña_nueva != contraseña_confirmada:
                messagebox.showwarning("Advertencia","La contraseña nueva no coincide")
                return
            
            #Se cifra la contraseña actual para poder compararla con la de la base de datos
            contraseña_actual = Cifrar_Contraseña(contraseña_actual)
            #Una vez confirmada la contraseña en cifrada
            contraseña_cifrada = Cifrar_Contraseña(contraseña_confirmada)
            
            bd = BaseDeDatos(host="localhost",user="root",password="Soydeboca66",database="Farmacia")
            bd.CrearConexion()

            query_verificar = "SELECT u.Contraseña,c.DNI FROM Usuarios u JOIN Clientes c ON u.id_usuario = c.id_usuario WHERE c.DNI = %s;"

            resultados = bd.ObtenerDatos(query_verificar,(self.dni_cliente,))

            #Verificamos que nos lleguen los datos y comparamos las contraseñas con los resultados
            if not resultados or resultados[0][0] != contraseña_actual:
                messagebox.showwarning("Advertencia","La contraseña actual es incorrecta")
                return
            
            #Se intentan insertar los datos
            try:
                query_actualizar = "UPDATE Usuarios u JOIN Clientes c ON u.id_usuario = c.id_usuario SET u.Contraseña = %s WHERE c.DNI = %s;"
                bd.Insertar_Datos(query_actualizar,(contraseña_cifrada,self.dni_cliente))
                messagebox.showinfo("Actulizar contraseña","Contraseña actualizada correctamente")
            #Se captura el error en caso de haberlo
            except Exception as err:
                print(err)

        #Diseño de la ventana
        vtn_contraseña = CTkToplevel()
        vtn_contraseña.title("Cambiar contraseña")
        vtn_contraseña.geometry("400x500")
        vtn_contraseña.resizable(0,0)

        frame_lateral = CTkFrame(vtn_contraseña,fg_color="blue2",width=500,height=100)
        frame_lateral.place(x=0)

        label_titulo = CTkLabel(frame_lateral,text="Cambiar contraseña",fg_color="blue2",font=("Arial",30,"bold"))
        label_titulo.place(x=60,y=30)

        entry_clave_actual = CTkEntry(vtn_contraseña,width=200,height=40,
                                       font=("Arial",16),
                                       placeholder_text="Contraseña actual",
                                       placeholder_text_color="gray",border_color="blue2")
        entry_clave_actual.place(x=100,y=150)

        entry_clave_nueva = CTkEntry(vtn_contraseña,width=200,height=40,
                                       font=("Arial",16),
                                       placeholder_text="Nueva contraseña",
                                       placeholder_text_color="gray",border_color="blue2")
        entry_clave_nueva.place(x=100,y=205)

        entry_confirmar_clave = CTkEntry(vtn_contraseña,width=200,height=40,
                                       font=("Arial",16),
                                       placeholder_text="Confirmar contraseña",
                                       placeholder_text_color="gray",border_color="blue2")
        entry_confirmar_clave.place(x=100,y=260)

        boton_cambiar = CTkButton(vtn_contraseña,text="Actualizar",fg_color="blue2",text_color="white",height=40,width=200,font=("Arial",14),command=Cambiar_Contraseña)
        boton_cambiar.place(x=100,y=310)

        boton_salir = CTkButton(vtn_contraseña,text="Atrás",fg_color="blue2",text_color="white",height=40,width=200,font=("Arial",14),command=Retroceder)
        boton_salir.place(x=100,y=360)

    
    def Salir_Ventana(self):
        opcion = messagebox.askokcancel("Salir","¿Esta seguro que desea salir del programa?")

        if opcion:
            sys.exit()