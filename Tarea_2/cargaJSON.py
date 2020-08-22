import json

carga = []
 
def cargaJson():
    with open('archivoJSON.json') as file:
        carga = json.load(file)

        print("         *************************")
        print("         Datos del archivo cargado")     
        print("         *************************")
 
        print("         Tipo de Estructura: ", type(carga))
        print("")

        for element in carga:                           
            print("         Nombre: ", element['Nombre'])
            print("         Edad: ", element['Edad'])
            print("         Telefono: ", element['Telefono'])
            print("         Direccion: ", element['Direccion'])
            print("")
            



