import mysql.connector

#Esta clase permite interactuar con la base de datos
class BaseDeDatos():
    #El constructor recibe como parametro los datos del motor
    def __init__(self,host,user,password,database):
        self.host = host
        self.user = user
        self.password = password
        self.database = database
        self.connection = None #Se definen ambos como None porque aun no se inicializan
        self.cursor = None
        
    #Se este metodo conectara con la base de datos
    def CrearConexion(self):
        #try para probar la conexion
        try:
            #Al atributo "connection" definido como None anteriormente se le asignan los valores
            self.connection = mysql.connector.connect(
                host= self.host,
                user = self.user,
                password = self.password,
                database = self.database
            )
            #al ya asignar los datos al atributo connection ya podemos utilizar
            #el atributo cursor
            self.cursor = self.connection.cursor()
            print("Conexion Realizada Exitosamente")
        #en caso de no funcionar lanzamos un error
        except mysql.connector.Error as err:
            print("Error al conectar con la base de datos ",err)
    
    #Cierra la conexion (Lo dice en el nombre no hace falta que lo escriba)
    def CerrarConexion(self):
        if self.cursor:
            self.cursor.close()
        if self.connection:
            self.connection.close()
        print("Conexion Cerrada Correctamente")
    
    #Esta funcion obtendra los datos de la BD
    def ObtenerDatos(self,query,params):
        #Primero se verificar que la conexion exista, ya que de esta depende
        #la ejecucion de la consulta
        if self.connection is None or self.cursor is None:
            print("Error de conexion")
            return None
        #Probamos con la consulta
        try:
            self.cursor.execute(query,params)
            resultados = self.cursor.fetchall()
            
            #Se retornan los datos para luego visualizarlos en una tabla
            return resultados
        except mysql.connector.Error as err:
            print("Se ha producido un error al obtener los datos",err)
    
    def Insertar_Datos(self,query,params):
        if self.connection is None or self.cursor is None:
            print("Error de conexion")
            return None
        
        try:
            self.cursor.execute(query,params)
            self.connection.commit()
            print("Datos insertados correctamente")
        
        except mysql.connector.Error as err:
            print("Error al insertar los datos",err)

    def Obtener_Id_Usuario(self):
        if self.connection is None is self.cursor in None:
            print("Error en la conexion")
            return None
        
        try:
            self.cursor.execute("SELECT LAST_INSERT_ID()")
            ultimo_id = self.cursor.fetchone()[0]
            return ultimo_id
        
        except mysql.connector.Error as err:
            print("Error al obtener el ID del usuario",err)
            return None


# bd = BaseDeDatos(host="localhost",user="root",password="Soydeboca66",database="Farmacia")
# bd.CrearConexion()

# nombre = input("Ingrese su nombre: ")
# apellido = input("Ingrese su apellido: ")
# direccion = input("Ingrese su direccion: ")
# username = nombre + apellido
# dni = int(input("Ingrese su DNI: "))
# contraseña = input("Ingrese su contraseña: ")

# query = "INSERT INTO Clientes (Nombre,Apellido,Direccion,DNI,Username,Contraseña) VALUES (%s,%s,%s,%s,%s,%s)"

# bd.Insertar_Datos(query, (nombre,apellido,direccion,dni,username,contraseña))

# bd.CerrarConexion()