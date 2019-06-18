import sqlite3

nom = str(input("Ingrese nombre->"))
ape = str(input("Ingrese apellido->"))
dis = str(input("Ingrese el distrito->"))
dir = str(input("Ingrese el direccion->"))
nt = float(input("Ingrese nota->"))

lista = [nom,ape,dis,dir,nt]

miConexion=sqlite3.connect("bdalumno")

miCursor= miConexion.cursor()

miCursor.execute('''CREATE TABLE 
                    IF NOT EXISTS 
                    alumno (
                    codigo varchar(45)  primary key,
                    nombre varchar(45),
                    apellido varchar(45),
                    distrito varchar(45),
                    direccion varchar(45),
                    nota double)
                 ''')



alumnos= [
#("P001","Roberto","Orellana","Santa anita","Calle 20",10),
#("P002","Diego","lujan","ate","Calle 20",20),
#("P003","Cindy","Gomez","Los Olivos","Calle 20",15),
#("P004","Gabriel","Castro","Huachipa","Calle 20",12),
#("P005","jorge","Ortega","Los Olivos","Calle 20",13),
#("P006","carla","Orellana","Santa anita","Calle 20",10),
#("P007","marta","lujan","ate","Calle 20",20),
#("P008","mercedes","Gomez","Los Olivos","Calle 20",15),
#("P009","virginia","Castro","Huachipa","Calle 20",12),
#("P010","soledad","Ortega","Los Olivos","Calle 20",13),
#("P011","Robert","Orellana","Santa anita","Calle 20",10),
#("P012","marco","lujan","ate","Calle 20",20),
#("P013","miguel","Gomez","Los Olivos","Calle 20",15),
#("P014","Gaby","Castro","Huachipa","Calle 20",12),
#("P015","alex","Ortega","Los Olivos","Calle 20",13),
#("P016","katty","Orellana","Santa anita","Calle 20",10),
#("P017","consuelo","lujan","ate","Calle 20",20),
#("P018","monica","Gomez","Los Olivos","Calle 20",15),
#("P019","rosa","Castro","Huachipa","Calle 20",12),
#("P020","marina","Ortega","Los Olivos","Calle 20",13),
]

miCursor.executemany("INSERT INTO alumno VALUES(?,?,?,?,?,?)",lista)

#Listar registros
miCursor.execute("SELECT * FROM alumno")
miCursor.execute("drop alumno")
lista1 = miCursor.fetchall()
print(lista1)



miConexion.commit()
miConexion.close()