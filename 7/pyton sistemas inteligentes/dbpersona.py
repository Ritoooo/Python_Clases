import sqlite3
import datetime

miConexion=sqlite3.connect("bdpersona")

miCursor= miConexion.cursor()

miCursor.execute('''CREATE TABLE 
                    IF NOT EXISTS 
                    persona (
                    id CHAR(4) primary key, 
                    nombre varchar(45),
                    apellido varchar(45),
                    distrito varchar(45),
                    direccion varchar(45),
                    sueldo double)
                 ''')

import sqlite3

miConexion=sqlite3.connect("bdpersona")

miCursor= miConexion.cursor()

miCursor.execute('''CREATE TABLE 
                    IF NOT EXISTS 
                    factura (
                    codigo char(4)  primary key,
                    raz varchar(45),
                    fecha datetime,
                    subtotal double,
                    igv double,
                    total double,
                    FOREIGN KEY (raz) REFERENCES persona(id))
                 ''')

personas= [
("P006","Roberto","Orellana","Santa anita","Calle 20",1000),
("P007","Diego","lujan","ate","Calle 20",2000),
("P008","Cindy","Gomez","Los Olivos","Calle 20",1500),
("P009","Gabriel","Castro","Huachipa","Calle 20",1200),
("P010","jorge","Ortega","Los Olivos","Calle 20",7000),
]

#miCursor.executemany("INSERT INTO persona(id,nombre,apellido,distrito,direccion,sueldo ) VALUES(?,?,?,?,?,?)",personas)


#Listar registros
miCursor.execute("SELECT * FROM persona")
lista1 = miCursor.fetchall()
print(lista1)

#Listar registros sueldos 100 a 5000
miCursor.execute("SELECT * FROM persona WHERE sueldo BETWEEN '100' AND '5000' ")
lista2 = miCursor.fetchall()
print(lista2)

#Listar registros sueldos 100 a 5000 y vive en los olivos
miCursor.execute("SELECT * FROM persona WHERE sueldo BETWEEN '100' AND '5000' and distrito='Los Olivos' ")
lista3 = miCursor.fetchall()
print(lista3)

#Listar registros promedio sueldos
miCursor.execute("SELECT sum(sueldo)/2,AVG(sueldo), min(sueldo), max(sueldo) FROM persona")
lista4 = miCursor.fetchall()
print(lista4)

#Listarmonto total vendido y su promedio
miCursor.execute("SELECT sum(sueldo)/2,AVG(sueldo), min(sueldo), max(sueldo) FROM persona")
lista4 = miCursor.fetchall()
print(lista4)



personas= [
#("001","Roberto","Orellana","Santa anita","Calle 20",1000),
#("002","Diego","lujan","ate","Calle 20",2000),
#("003","Cindy","Gomez","Los Olivos","Calle 20",1500),
#("004","Gabriel","Castro","Huachipa","Calle 20",1200),
#("005","jorge","Ortega","Los Olivos","Calle 20",7000),
#("005","jorge","Ortega","Los Olivos","Calle 20",7000),
]

dt = datetime.datetime.now()
facturas= [
#("F001", "P001", dt, 800, 144, 944),
#("F002", "P002", dt, 400, 72, 472),
#("F003", "P003", dt, 200, 36, 236),
#("F004", "P004", dt, 100, 18, 118),
#("F005", "P005", dt, 20000, 3600, 23600),
#("F006", "P006", dt, 10000, 1800, 11800),
]
miCursor.executemany("INSERT INTO factura VALUES(?,?,?,?,?,?)",facturas)


#Listar registros
miCursor.execute("SELECT * FROM persona")
lista1 = miCursor.fetchall()
print(lista1)

#Listar registros sueldos 100 a 5000
miCursor.execute("SELECT * FROM persona WHERE sueldo BETWEEN '100' AND '5000' ")
lista2 = miCursor.fetchall()
print(lista2)

#Listar registros sueldos 100 a 5000 y vive en los olivos
miCursor.execute("SELECT * FROM persona WHERE sueldo BETWEEN '100' AND '5000' and distrito='Los Olivos' ")
lista3 = miCursor.fetchall()
print(lista3)

#Listar registros promedio sueldos
miCursor.execute("SELECT sum(sueldo)/2,AVG(sueldo), min(sueldo), max(sueldo) FROM persona")
lista4 = miCursor.fetchall()
print(lista4)

#Listar monto total vendido y su promedio
miCursor.execute("SELECT sum(sueldo)/2,AVG(sueldo), min(sueldo), max(sueldo) FROM persona")
lista4 = miCursor.fetchall()
print(lista4)

#Listarclientes de monto entre 10 y 4000
miCursor.execute("SELECT p.id,p.nombre,total FROM factura as f join persona as p on p.id = f.raz where f.total between '10' and '4000'")
lista4 = miCursor.fetchall()
print(lista4)


miConexion.commit()

miConexion.close()
