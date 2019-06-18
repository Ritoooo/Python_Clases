import sqlite3

miConexion=sqlite3.connect("bdgestionproducto")

miCursor= miConexion.cursor()

miCursor.execute('''CREATE TABLE 
                    IF NOT EXISTS 
                    PRODUCTOS (codpro CHAR(4) primary key, 
                    nom varchar(45),
                    precio double)
                 ''')

productos= [
("P001","lacteo",5.50),
("P002","carnes",18.50),
("P003","agua cielo",20.50),
("P004","agua san carlos",2.50),
("P005","leche",90.50)
]

miCursor.executemany("INSERT INTO PRODUCTOS VALUES(?,?,?)",productos)


miConexion.commit()

miConexion.close()

