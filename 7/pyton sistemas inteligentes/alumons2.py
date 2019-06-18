import sqlite3
nom = str(input("Ingrese nombre->"))
ape = str(input("Ingrese apellido->"))
dis = str(input("Ingrese el distrito->"))
dir = str(input("Ingrese el direccion->"))
nt = float(input("Ingrese nota->"))

lista = [nom,ape,dis,dir,nt]

miConexion=sqlite3.connect("bdalumno")

miCursor= miConexion.cursor()

miCursor.execute('''create TABLE 
                    IF NOT EXISTS 
                    alumnos (
                    nombre varchar(45)  primary key,
                    apellido varchar(45),
                    distrito varchar(45),
                    direccion varchar(45),
                    nota double)
                 ''')



alumnos= [
#("Roberto","Orellana","Santa anita","Calle 20",10),
#("Diego","lujan","ate","Calle 20",20),
#("P003","Cindy","Gomez","Los Olivos","Calle 20",15),
#("P004","Gabriel","Castro","Huachipa","Calle 20",12),
#("P005","jorge","Ortega","Los Olivos","Calle 20",13),
#("P006","carla","Orellana","Santa anita","Calle 20",10),
#("P007","marta","lujan","ate","Calle 20",20),

]

miCursor.executemany("INSERT INTO alumnos VALUES(?,?,?,?,?)",lista)

#Listar registros
miCursor.execute("SELECT * FROM alumnos")
#miCursor.execute("drop alumno")
lista1 = miCursor.fetchall()
print(lista1)




miConexion.commit()

miConexion.close()