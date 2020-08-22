import csv

carga = []

def cargaCsv():

    with open('archivoCSV.csv') as file:
        dato = csv.DictReader(file, delimiter=';')
        
        print("         *************************")
        print("         Datos del archivo cargado")     
        print("         *************************")

        print("         Tipo de Estructura: ", type(carga))
        print("")
        
        for element in dato:
            print("         Nombre: ",element['nombre'])
            print("         Edad: ",element['edad'])
            print("         Telefono: ",element['telefono']) 
            print("         Direccion: ",element['direccion'])
            print("")

            

       

        

        

        

        