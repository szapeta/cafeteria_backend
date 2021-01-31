import db

tabla = "info"

def getInfo():
    sqlCampos = 'nombre, version, fecha'
    condicion = ""
    jsonResp = []

    datos = db.select(sqlCampos, tabla, condicion)

    for dato in datos:
        jsonResp.append({"nombre:":dato[0], "version":dato[1], "fecha":dato[2]})
    return jsonResp
