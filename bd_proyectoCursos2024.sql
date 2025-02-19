/*Creacion de la base de datos */
CREATE DATABASE Farmacia;

/*Se la utiliza*/
USE Farmacia;

CREATE TABLE Usuarios(
id_usuario INT PRIMARY KEY AUTO_INCREMENT,
Username VARCHAR(50) NOT NULL,
Contraseña VARCHAR(50) NOT NULL,
Rol INT NOT NULL
);

/*Tabla donde se almacenara la informacion de los clientes*/
CREATE TABLE Clientes(
id_cliente INT PRIMARY KEY AUTO_INCREMENT,
id_usuario INT NOT NULL, 
Nombre VARCHAR(50) NOT NULL,
Apellido VARCHAR(50) NOT NULL,
Direccion VARCHAR (50) NOT NULL,
Telefono VARCHAR (15) NOT NULL,
DNI INT NOT NULL UNIQUE,
Obra_Social VARCHAR (30) NULL,
FOREIGN KEY (id_usuario) REFERENCES Usuarios(id_usuario)
);

/*Tabla donde se almacena la informacion de los pedidos realizados por los clientes*/
CREATE TABLE Pedidos(
id_pedido INT PRIMARY KEY AUTO_INCREMENT,
Fecha_Pedido DATE NOT NULL,
Total DECIMAL (10,2) NOT NULL,
Estado ENUM('Aceptado','Pendiente','Rechazado') DEFAULT ('Pendiente'),
Metodo_Pago ENUM ('Efectivo','Debito','Credito') DEFAULT ('Efectivo'),
id_cliente INT NOT NULL,
FOREIGN KEY (id_cliente) REFERENCES Clientes(id_cliente)
);

/*Tabla con informacion de los medicamentos*/
CREATE TABLE Medicamentos(
id_medicamento INT PRIMARY KEY AUTO_INCREMENT,
Nombre VARCHAR(50) NOT NULL,
Descripcion VARCHAR (100) NULL,
Precio DECIMAL (10,2) NOT NULL,
Categoria ENUM ('Analgesicos','Antibioticos','Antiinflamatorios','Antialergicos','Antivirales') NULL,
Stock INT NOT NULL
);

/*Tabla para almacenar el detalle de los pedidos de los clientes*/
CREATE TABLE Detalle_Pedidos(
id_detalle INT PRIMARY KEY AUTO_INCREMENT,
Cantidad INT NOT NULL,
id_pedido INT NOT NULL,
id_medicamento INT NOT NULL,
FOREIGN KEY (id_pedido) REFERENCES Pedidos(id_pedido),
FOREIGN KEY (id_medicamento) REFERENCES Medicamentos(id_medicamento)
);

CREATE TABLE Empleados(
id_empleado INT PRIMARY KEY AUTO_INCREMENT,
id_usuario INT NOT NULL,
Nombre VARCHAR (50) NOT NULL,
Apellido VARCHAR(50) NOT NULL,
Direccion VARCHAR (50) NOT NULL,
Telefono VARCHAR (50) NOT NULL,
DNI INT UNIQUE NOT NULL,
Sueldo DECIMAL (10,2) NOT NULL,
FOREIGN KEY (id_usuario) REFERENCES Usuarios(id_usuario)
);

USE Farmacia;
SELECT * FROM Pedidos;
SELECT * FROM Detalle_Pedidos;
SELECT * FROM Medicamentos;

SELECT dp.Cantidad 
FROM Detalle_Pedidos dp
JOIN Medicamentos m ON dp.id_medicamento = m.id_medicamento
JOIN Pedidos p ON dp.id_pedido = p.id_pedido
WHERE m.Nombre = 'Tafirol Plus' AND p.id_pedido = 26;

USE Farmacia;
SELECT * FROM Usuarios;

SELECT u.Rol, c.DNI 
FROM Usuarios u 
LEFT JOIN Clientes c ON u.id_usuario = c.id_usuario 
WHERE u.Username = 'Admin' AND u.Contraseña = '4567';


SELECT * FROM Empleados;
SELECT * FROM Usuarios;


INSERT INTO Usuarios (Username,Contraseña,Rol)
VALUES
('LuisLiberal2212','vivalalibertad',2);