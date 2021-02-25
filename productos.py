import db

tabla = "Producto"

def getallproducts():
    sqlCampos = 'idProducto, Nombre, Descripcion, Precio, Imagen'
    condicion = " Estado = 1"
    jsonResp = []

    datos = db.select(sqlCampos, tabla, condicion)

    for dato in datos:
        jsonResp.append({"idProducto:":dato[0], "Nombre":dato[1], "Descripcion":dato[2], "Precio":str(dato[3]), "Imagen":dato[4]})
    return jsonResp