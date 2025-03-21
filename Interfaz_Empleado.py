from customtkinter import *
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from ConexionBD import BaseDeDatos
import random
from Cifrado import Cifrar_Contraseña

#Clase que contiene el diseño de la ventana empleados
class Ventana_Empleado:
    def __init__(self,root,rol,vtn_empleado,dni_empleado):
        self.root = root
        self.rol = rol
        self.dni_empleado = dni_empleado
        self.root.title("Ventana Empleados")
        self.root.geometry("790x400")
        self.root.resizable(0,0)

        self.vtn_empleado = vtn_empleado


        set_appearance_mode("dark")
        set_default_color_theme("blue")

        #Diseño de la barra lateral de la ventana
        self.frame_lateral = CTkFrame(self.root,fg_color="black",width=250,height=800)
        self.frame_lateral.place(x=0)

        self.label_titulo = CTkLabel(self.root,text="Menu Empleado",font=("Verdana",20,"bold"),fg_color="black")
        self.label_titulo.place(x=40,y=10)

        self.label_id_pedido = CTkLabel(self.root,text="ID Pedido",font=("Verdana",15,"bold"),fg_color="black")
        self.label_id_pedido.place(x=10,y=60)

        self.entry_id_pedido = Entry(self.root)
        self.entry_id_pedido.place(x=100,y=65)

        self.label_total = CTkLabel(root,text=f"Total del Pedido: ",text_color="white",font=("verdana",30))
        self.label_total.place(x=260,y=330)

        self.boton_confirmar = CTkButton(self.root,text="Confirmar Compra",fg_color="blue2",font=("Arial",15,),width=150,height=40,command=self.Confirmar_Compra)
        self.boton_confirmar.place(x=260,y=250)

        self.boton_cancelar = CTkButton(self.root,text="Cancelar Compra",fg_color="blue2",font=("Arial",15,),width=150,height=40,command=self.Cancelar_Compra)
        self.boton_cancelar.place(x=420,y=250)

        self.boton_limpiar = CTkButton(self.root,text="Limpiar Tabla",fg_color="blue2",font=("Arial",15),width=150,height=40,command=self.Limpiar_Tabla)
        self.boton_limpiar.place(x=580,y=250)

        self.boton_buscar = CTkButton(self.frame_lateral,text="BUSCAR",fg_color="blue2",width=185,command=self.Obtener_Datos)
        self.boton_buscar.place(x=40,y=100)
        
        self.boton_contreñas = CTkButton(self.frame_lateral,text="RESTABLECER CONTRASEÑA",fg_color="blue2",command=self.Restablecer_Contraseña)
        self.boton_contreñas.place(x=40,y=130)

        self.boton_Stock = CTkButton(self.frame_lateral,text="ACTUALIZAR STOCK",fg_color="blue2",width=185,command=self.Ventana_Actualizar_Stock)
        self.boton_Stock.place(x=40,y=160)

        boton_cambiarContraseña = CTkButton(self.frame_lateral,text="CAMBIAR CONTRASEÑA",width=185,fg_color="blue2",command=self.Ventana_Contraseña)
        boton_cambiarContraseña.place(x=40,y=290)

        self.boton_salir = CTkButton(self.frame_lateral,text="SALIR",fg_color="blue2",width=185,command=self.Salir)
        self.boton_salir.place(x=40,y=320)
        
        columnas = ("Medicamento","Cantidad","Metodo De Pago","Estado")

        #Diseño de la seccion donde se implementara la tabla
        self.tabla = ttk.Treeview(self.root,columns=columnas,show="headings")

        self.tabla.heading("Medicamento",text="Medicamento")
        self.tabla.heading("Cantidad",text="Cantidad")
        self.tabla.heading("Metodo De Pago",text="Metodo De Pago")
        self.tabla.heading("Estado",text="Pago")

        self.tabla.column("Medicamento",width=130,anchor="center")
        self.tabla.column("Cantidad",width=130,anchor="center")
        self.tabla.column("Metodo De Pago",width=130,anchor="center")
        self.tabla.column("Estado",width=130,anchor="center")

        self.tabla.place(x=255,y=10)
    
    def Confirmar_Compra(self):
        bd = BaseDeDatos(host="localhost",user="root",password="Soydeboca66",database="Farmacia")
        bd.CrearConexion()

        query_ActualizarEstado = "UPDATE Pedidos SET Estado = 'Aceptado' WHERE id_pedido = %s;"

        query_VerificarStock = "SELECT Nombre FROM Medicamentos WHERE Stock = 0;"

        resultados_stock = bd.ObtenerDatos(query_VerificarStock,())

        #Esta consulta obtiene la cantidad de cada medicamento solicitado en cada pedido
        query_cantidad = "SELECT m.Nombre,m.id_medicamento,dp.Cantidad,dp.id_pedido FROM Medicamentos m JOIN Detalle_Pedidos dp ON m.id_medicamento = dp.id_medicamento WHERE dp.id_pedido = %s;"

        id_detallePedido = self.entry_id_pedido.get()
        resultados = bd.ObtenerDatos(query_cantidad,(id_detallePedido,))
        
        query_consultarEstado = "SELECT id_pedido,Estado FROM Pedidos WHERE id_pedido = %s;"
        resultados_estado = bd.ObtenerDatos(query_consultarEstado,(id_detallePedido,))

        if resultados_estado[0][1] == 'Aceptado':
            messagebox.showwarning("Advertencia","El pedido ingresado ya fue aceptado")
            print(resultados_estado)
            return
        
        if resultados_estado[0][1] == 'Rechazado':
            messagebox.showwarning("Advertencia","El pedido que intenta aceptar fue rechazado")
            return
        
        if resultados_stock:
            nombres = ""
            for i in resultados_stock:
                nombres += i[0] + "\n"
            messagebox.showwarning("Advertencia",f"Los siguientes medicamentos no tienen stock:\n{nombres}")
            return

        if not resultados:
            messagebox.showwarning("Advertencia","No se encontraron productos")
            return
        
        try:
            for nombre,id_medicamento, cantidad, id_pedido in resultados:
                query_actualizacion = "UPDATE Medicamentos SET Stock = Stock - %s WHERE id_medicamento = %s AND Stock >= %s;"

                bd.Insertar_Datos(query_actualizacion,(cantidad,id_medicamento,cantidad))
                bd.Insertar_Datos(query_ActualizarEstado,(id_detallePedido,))
            messagebox.showinfo("Informacion","Compra finalizada correctamente")
            self.Limpiar_Tabla()
        except Exception as err:
            print(err)

    def Cancelar_Compra(self):
        bd = BaseDeDatos(host="localhost",user="root",password="Soydeboca66",database="Farmacia")
        bd.CrearConexion()

        id_pedido = self.entry_id_pedido.get()

        query_consultarEstado = "SELECT id_pedido,Estado FROM Pedidos WHERE id_pedido = %s;"
        resultados_Estado = bd.ObtenerDatos(query_consultarEstado,(id_pedido,))

        try:
            if resultados_Estado[0][1] != 'Aceptado':
                query_actualizarEstado = "UPDATE Pedidos SET Estado = 'Rechazado' WHERE id_pedido = %s;"
                bd.Insertar_Datos(query_actualizarEstado,(id_pedido,))
                messagebox.showinfo("Informacion","El pedido fue cancelado exitosamente")
            else:
                messagebox.showwarning("Advertencia","El pedido no puede ser cancelado porque ya fue aceptado")
        except Exception as err:
            print(err)
        

    def Obtener_Datos(self):
        bd = BaseDeDatos(host="localhost",user="root",password="Soydeboca66",database="Farmacia")
        bd.CrearConexion()

        id_pedido = self.entry_id_pedido.get()

        query = "SELECT m.Nombre AS Nombre_Producto,dp.Cantidad,p.Metodo_pago,p.Estado,p.Total FROM Pedidos p JOIN Detalle_Pedidos dp ON p.id_pedido = dp.id_pedido JOIN Medicamentos m ON dp.id_medicamento = m.id_medicamento WHERE p.id_pedido = %s"
        try:
            resultados = bd.ObtenerDatos(query,(id_pedido,))
            self.tabla.delete(*self.tabla.get_children())

            if not id_pedido:
                messagebox.showwarning("Advertencia","Por favor ingrese un ID de pedido")
                return

            if resultados:
                total_pedido = resultados[0][-1]
                self.label_total.configure(text=f"Total del Pedido: ${total_pedido:,.2f}")

                for datos in resultados:
                    self.tabla.insert("","end",values=datos[:-1])
                # for datos in resultados:
                #     self.tabla.insert("","end",values=datos)
            else:
                messagebox.showwarning("Advertencia","ID de pedido inexistente")
                self.entry_id_pedido.delete(0,END)
        except Exception as err:
            messagebox.showerror("Error","Error interno al obtener los datos")
            print(err)
    
    def Ventana_Contraseña(self):
        self.root.withdraw()

        def Retroceder():
            vtn_contraseña.destroy()
            self.root.deiconify()
        
        def Cambiar_Contraseña():
            bd = BaseDeDatos(host="localhost",user="root",password="Soydeboca66",database="Farmacia")
            bd.CrearConexion()
            
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
            

            query_verificar = "SELECT u.Contraseña,e.DNI FROM Usuarios u JOIN Empleados e ON u.id_usuario = e.id_usuario WHERE e.DNI = %s;"

            resultados = bd.ObtenerDatos(query_verificar,(self.dni_empleado,))

            #Verificamos que nos lleguen los datos y comparamos las contraseñas con los resultados
            if not resultados or resultados[0][0] != contraseña_actual:
                messagebox.showwarning("Advertencia","La contraseña actual es incorrecta")
                return
            
            #Se intentan insertar los datos
            try:
                query_actualizar = "UPDATE Usuarios u JOIN Empleados c ON u.id_usuario = c.id_usuario SET u.Contraseña = %s WHERE c.DNI = %s;"
                bd.Insertar_Datos(query_actualizar,(contraseña_cifrada,self.dni_empleado))
                messagebox.showinfo("Actulizar contraseña","Contraseña actualizada correctamente")
                entry_clave_actual.delete(0,END)
                entry_clave_nueva.delete(0,END)
                entry_confirmar_clave.delete(0,END)
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
    
    def Ventana_Actualizar_Stock(self):
        def Actualizar_Stock():
                medicamento_nombre = lista_medicamentos.get()

                id_medicamento = None
                for nombre,id_med in medicamentos_d:
                    if nombre == medicamento_nombre:
                        id_medicamento = id_med
                        break
                
                try:
                    nuevo_stock = entry_stock.get()
                    query = "UPDATE Medicamentos SET Stock = %s WHERE id_medicamento = %s"
                    bd.Insertar_Datos(query,(nuevo_stock,id_medicamento))
                    messagebox.showinfo("Informacion","Stock actualizado correctamente")
                    entry_stock.delete(0,END)
                except Exception as err:
                    print(err)
        
        self.root.withdraw()
        bd = BaseDeDatos(host="localhost",user="root",password="Soydeboca66",database="Farmacia")
        bd.CrearConexion()
        #Diseño de la ventana
        vtn_stock = CTkToplevel()
        vtn_stock.title("Actualizar Stock")
        vtn_stock.geometry("400x500")
        vtn_stock.resizable(0,0)
        
        self.vtn_empleado.withdraw()

        frame_titulo = CTkFrame(vtn_stock,fg_color="blue2",width=400,height=100)
        frame_titulo.place(x=0)

        label_titulo = CTkLabel(frame_titulo,text="Actualizar Stock",fg_color="blue2",font=("Arial",25,"bold"))
        label_titulo.place(x=100,y=30)

        query = "SELECT id_medicamento,Nombre FROM Medicamentos;"
        medicamentos = bd.ObtenerDatos(query,())

        medicamentos_d = [(medicamento[1],medicamento[0]) for medicamento in medicamentos]

        medicamentos_nombres = [medicamento[0] for medicamento in medicamentos_d]

        lista_medicamentos = CTkComboBox(vtn_stock,values=medicamentos_nombres,width=200,height=40,border_color="blue2")
        lista_medicamentos.place(x=100,y=120)

        entry_stock = CTkEntry(vtn_stock,width=200,height=40,
                                       font=("Arial",16),
                                       placeholder_text="Stock",
                                       placeholder_text_color="gray",border_color="blue2")
        entry_stock.place(x=100,y=170)

        boton_actualizar = CTkButton(vtn_stock,text="Actualizar",width=200,height=40,font=("Segoe UI",20),fg_color="blue2",command=Actualizar_Stock)
        boton_actualizar.place(x=100,y=220)

        boton_atras = CTkButton(vtn_stock,text="Atrás",width=200,height=40,font=("Segoe UI",20),fg_color="blue2",command=lambda: self.Retroceder(vtn_stock))
        boton_atras.place(x=100,y=270)


    def Restablecer_Contraseña(self):

        def Generar_Contraseña():
            bd = BaseDeDatos(host="localhost",user="root",password="Soydeboca66",database="Farmacia")
            bd.CrearConexion()
            dni = entry_dni.get()
            longitud = 6
            caracteres = "abcdefghijklmnñopqrstuvwxyzABCDEFGHIJKLMNÑOPQRSTUVWXYZ0123456789"
            lista_caracteres = list(caracteres)
            clave = ""

            i = 0
            while i < longitud:
                clave = clave + random.choice(lista_caracteres)
                i = i + 1
            
            clave_cifrada = Cifrar_Contraseña(clave)
            try:
                query = "UPDATE Usuarios u JOIN Clientes c ON c.id_usuario = u.id_usuario SET u.Contraseña = %s WHERE c.DNI = %s;"
                resultados = bd.Insertar_Datos(query,(clave_cifrada,dni))
                if resultados:    
                    messagebox.showinfo("Restablecer Contraseña","Contraseña generada exitosamente")
                    messagebox.showinfo("Restablecer Contraseña",f"Su contraseña es {clave}")
                    entry_dni.delete(0,END)
                else:
                    messagebox.showwarning("Restablecer Contraseña","Error DNI inexistente")
            except Exception as err:
                messagebox.showerror("Error interno al actualizar los datos")
                print(err)
            finally:
                bd.CerrarConexion()
            
        #Diseño de la ventana
        self.root.withdraw()
        vtn_contraseña = CTkToplevel()
        vtn_contraseña.title("Restablecer Contraseña")
        vtn_contraseña.geometry("400x350")
        vtn_contraseña.resizable(0,0)

        frame_titulo = Frame(vtn_contraseña,bg="blue2",width=400,height=100)
        frame_titulo.place(x=0)

        label_titulo = CTkLabel(frame_titulo,text="Restablecer Contraseña",fg_color="blue2",font=("Arial",25,"bold"))
        label_titulo.place(x=60,y=30)

        entry_dni = CTkEntry(vtn_contraseña,width=200,height=40,
                                       font=("Arial",16),
                                       placeholder_text="DNI",
                                       placeholder_text_color="gray",border_color="blue2")
        entry_dni.place(x=100,y=120)

        boton_restablecer = CTkButton(vtn_contraseña,text="Restablecer",fg_color="blue2",text_color="white",height=40,width=200,font=("Arial",14),command=Generar_Contraseña)
        boton_restablecer.place(x=100,y=170)

        boton_atras = CTkButton(vtn_contraseña,text="Atrás",fg_color="blue2",text_color="white",height=40,width=200,font=("Arial",14),command=lambda: self.Retroceder(vtn_contraseña))
        boton_atras.place(x=100,y=215)

    def Limpiar_Tabla(self):
        self.tabla.delete(*self.tabla.get_children())
        self.label_total.configure(text=f"Total del Pedido: $0.00")

    def Retroceder(self,ventana):
        ventana.destroy()
        self.root.deiconify()

    def Salir(self):
        opcion = messagebox.askokcancel("Salir","¿Esta seguro de que desea salir?")
        if opcion:
            self.root.destroy()