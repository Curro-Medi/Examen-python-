from Clases1 import conexion, insertardatos, creartabla, selecttornillos

archivo = "ERP_FESAC.db"
con = conexion(archivo)
cur = con.cursor()

respuesta = input("Si quiere crear las tablas escriba si\n")

if respuesta == "si" :
    creartabla(con)

respuesta = input("Si quiere insertar los datos escriba si\n")

if respuesta == "si" :
    insertardatos(con)

respuesta = input("Si quiere ver los tornillos128 vendidos escriba si\n")
if respuesta == "si" :
    selecttornillos(con)
