import cargaJSON
import cargaXML
import cargaCSV

def menu(): 

    print("")
    print("         --------------------------------")
    print("         Cargar archivos [JSON--XML--CSV]")
    print("         --------------------------------")
    print("")
    print("         [1]Cargar JSON")
    print("         [2]Cargar XML")
    print("         [3]Cargar CSV")
    print("         [0]Salir")

    print("")
    opcion = input("    Ingrese una opcion: ")
    print("")

    if opcion == "1":
        cargaJSON.cargaJson()
        menu()
    elif opcion == "2":
        cargaXML.cargaXml()
        menu()
    elif opcion == "3":
        cargaCSV.cargaCsv()
        menu()
    elif opcion == "0":
        print("")
        print("     *-*-*-*Programa finalizado*-*-*-*")
        print("")
        exit()
    else:
        print("")
        print("     *****Error opcion incorrecta******")
        print("")
        menu()

menu()