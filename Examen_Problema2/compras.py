import sqlite3
from sqlite3 import Error
import csv

def conexion(filename = ":memory:"):
    try:
        con = sqlite3.connect(filename)
        print("Conexion realizada a ", filename)
    except Error:
        print(Error)
        con = None 
    finally:
        return con



def creartabla(con):
    try:
        cur = con.cursor()
        
        cur.execute("create table compras(id integer primary key, fecha text, cdgproducto text, proveedor integer, cantidad integer, precio real , importecompra text)") 
        con.commit()
        
        print("Tablas creada")
    
    except sqlite3.OperationalError:
        print("La tabla ya existia")

def insertardatos(con):
    try:
        cur = con.cursor()
        compras = tuple()
        
        fichero = open("compras.txt", "r")
        for linea in fichero:
            compras = linea.split(",")
            #print(compras)
            cur.execute("insert into compras values(" + compras[0] + "," + str(compras[1]) + "," + str(compras[2]) + "," + compras[3] + "," + compras[4] + "," + compras[5] + "," + str(compras[6]) + ");")
        
        fichero.close()
        con.commit()

        print("Datos insertados correctamentes")
    
    except sqlite3.IntegrityError as err:
        print("Error --> ", err )
        print("No se aniadieron los registros")

    


def actualizarcompras(con):
    try:
        
        cur = con.cursor()

        cur.execute("update compras set importecompra = precio * cantidad")
        con.commit()
            
        
    except sqlite3.OperationalError:
        print("Algo fue mal")



def importeencsv(con):
    
    cur = con.cursor()
    
    cur.execute("SELECT distinct(proveedor) from compras")
    proveedor = cur.fetchall()    
    dato = []
    dato.append(["Proveedor"] + ["Acumulado en compras"])

    cont = 0

    for i in proveedor:
        cur.execute("SELECT sum(importecompra) from compras where proveedor = (?)", i)
        cat = cur.fetchall()
        cont = cont + 1
        importecsv = open("Compras_Proveedor.csv","w")
        dato.append([cont] + [cat])

        with importecsv:
            writer = csv.writer(importecsv, delimiter=";")
            writer.writerows(dato)
        
        
    importecsv.close()
        
    con.commit()  

def importeencsv2(con):
    
    cur = con.cursor()
    
    cur.execute("SELECT distinct(cdgproducto) from compras")
    produ = cur.fetchall()    
    dato = []
    dato.append(["Producto"] + ["Precio"]+ ["Cantidad total"]+ ["Importe total"])

    for i in produ:
        cur.execute("SELECT distinct(precio) from compras where cdgproducto = (?)", i)
        cat = cur.fetchall()

        cur.execute("SELECT sum(cantidad) from compras where cdgproducto = (?)", i)
        cat2 = cur.fetchall()

        cur.execute("SELECT sum(importecompra) from compras where cdgproducto = (?)", i)
        cat3 = cur.fetchall()

        importecsv = open("Compras_Productos.csv","w")
        dato.append([i] + [cat] + [cat2] + [cat3])

        with importecsv:
            writer = csv.writer(importecsv, delimiter=";")
            writer.writerows(dato)
        
        
    importecsv.close()
        
    con.commit()  