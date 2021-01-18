from compras import conexion, creartabla, insertardatos, actualizarcompras, importeencsv,importeencsv2

archivo = "bd_compras.db"
con = conexion(archivo)
cur = con.cursor()

respuesta = input("Si quiere crear las tablas escriba si\n")

if respuesta == "si" :
    creartabla(con)
    insertardatos(con)
    actualizarcompras(con)



importeencsv(con)

importeencsv2(con)