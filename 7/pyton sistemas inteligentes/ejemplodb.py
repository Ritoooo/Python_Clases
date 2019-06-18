#Visor SQLIte, como el que tengo en el escritorio de este equipo
# En campos autoincrement agregar en el insert into el valor NULL
import sqlite3

miConexion=sqlite3.connect("bdcolegio")

miCursor= miConexion.cursor()

miCursor.execute('''CREATE TABLE 
                    IF NOT EXISTS 
                    CURSO (id int, nom varchar(45))
                 ''')
#miCursor.execute("INSERT INTO CURSO VALUES(1,'Matemática Básica')")

#Insertando varios Cursos
#variosCursos = [
#
#    (2,"Historia"),
#    (3,"Geografía"),
#    (4,"Lógico matemático")
#]

#miCursor.executemany("INSERT INTO CURSO VALUES(?,?)",variosCursos)

#Listar registros
miCursor.execute("SELECT * FROM CURSO")
varios = miCursor.fetchall()

#print(varios)

#Primera Forma
#for curso in varios:
#    print(curso)

#Segunda Forma
for curso in varios:
    print(curso[0]," ",curso[1])


miConexion.commit()

miConexion.close()
