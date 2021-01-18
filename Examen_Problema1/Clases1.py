import sqlite3
from sqlite3 import Error

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
        
        cur.execute("create table productos(id integer primary key, nombre text, preciocoste real, precioventa real, stockactual integer)") 
        con.commit()
   
        cur.execute("create table stock(cdgproducto text , almacen text , stock integer, foreign key (cdgproducto) references productos(nombre))") 
        con.commit()
        
        cur.execute("create table movimientos(id integer primary key, fecha text, cdgproducto text, almacen text, tipo text, cantidad integer, foreign key (cdgproducto) references productos(nombre))") 
        con.commit()
        
        print("Tablas creada")
    
    except sqlite3.OperationalError:
        print("La tablas ya existian")
     


def insertardatos(con):
    try:
        cur = con.cursor()
        productos = tuple()
        
        fichero = open("productos.txt", "r")
        for linea in fichero:
            productos = linea.split(",")
            #print(productos)
            cur.execute("insert into productos values(" + productos[0] + "," + str(productos[1]) + "," + productos[2] + "," + productos[3] + "," + productos[4] + ");")
        
        fichero.close()
        con.commit()


        stock = tuple()
        
        fichero2 = open("stock.txt", "r")
        for linea in fichero2:
            stock = linea.split(",")
            #print(stock)
            cur.execute("insert into stock values(" + str(stock[0]) + "," + str(stock[1]) + "," + stock[2] + ");")
        
        fichero2.close()
        con.commit()


        movimientos = tuple()
        
        fichero3 = open("movimientos.txt", "r")
        for linea in fichero3:
            movimientos = linea.split(",")
            #print(movimientos)
            cur.execute("insert into movimientos values(" + movimientos[0] + "," + str(movimientos[1]) + "," + str(movimientos[2]) + "," + str(movimientos[3]) + "," + str(movimientos[4]) + "," + movimientos[5] + ");")
        
        fichero3.close()
        con.commit()

        print("Datos insertados correctamentes")
    
    except sqlite3.IntegrityError as err:
        print("Error --> ", err )
        print("No se aniadieron los registros")

    
def selecttornillos(con):
    try:
        
        cur = con.cursor()
        print()
        print("Cantidad de tornillo128 vendidos: ")
        cur.execute("select cantidad from movimientos where cdgproducto = 'tornillo128' and tipo = 'venta'")
        rows = cur.fetchall()
        print(rows)     
        con.commit() 
    except sqlite3.OperationalError:
        print("Algo fue mal")
        
        